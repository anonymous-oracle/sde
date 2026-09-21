-- Northstar SQL Lab — schema v1 (PostgreSQL 15+; runs unchanged on Cloud SQL / AlloyDB for PostgreSQL)
DROP SCHEMA IF EXISTS lab CASCADE;
CREATE SCHEMA lab;
SET search_path = lab;
SET TIME ZONE 'UTC';

CREATE TABLE tenant (
  tenant_id   int         PRIMARY KEY,
  name        text        NOT NULL UNIQUE,
  plan        text        NOT NULL CHECK (plan IN ('free','pro','enterprise')),
  created_at  timestamptz NOT NULL
);

CREATE TABLE app_user (
  user_id      bigint      PRIMARY KEY,
  tenant_id    int         NOT NULL REFERENCES tenant,
  email        text        NOT NULL,
  display_name text        NOT NULL,
  country      char(2),                                   -- NULL on purpose (unknown)
  referred_by  bigint      REFERENCES app_user,           -- forest: recursive-CTE fodder
  created_at   timestamptz NOT NULL,
  deleted_at   timestamptz,                               -- soft delete
  UNIQUE (tenant_id, email),
  UNIQUE (tenant_id, user_id)                             -- target for tenant-safe composite FKs
);

CREATE TABLE category (
  category_id int  PRIMARY KEY,
  tenant_id   int  NOT NULL REFERENCES tenant,
  parent_id   int  REFERENCES category,
  name        text NOT NULL
);

CREATE TABLE product (
  product_id      bigint      PRIMARY KEY,
  tenant_id       int         NOT NULL REFERENCES tenant,
  sku             text        NOT NULL,
  name            text        NOT NULL,
  category_id     int         REFERENCES category,        -- NULL = uncategorised
  price_minor     int         NOT NULL CHECK (price_minor >= 0),   -- current list price, minor units
  currency        char(3)     NOT NULL DEFAULT 'USD',
  attrs           jsonb       NOT NULL DEFAULT '{}',
  created_at      timestamptz NOT NULL,
  discontinued_at timestamptz,
  UNIQUE (tenant_id, sku)
);

CREATE TABLE product_price_history (                      -- effective-dated prices (valid_from inclusive)
  product_id  bigint      NOT NULL REFERENCES product,
  valid_from  timestamptz NOT NULL,
  price_minor int         NOT NULL CHECK (price_minor >= 0),
  PRIMARY KEY (product_id, valid_from)
);

CREATE TABLE stock (
  product_id bigint      PRIMARY KEY REFERENCES product,
  on_hand    int         NOT NULL CHECK (on_hand >= 0),
  reserved   int         NOT NULL DEFAULT 0 CHECK (reserved >= 0),
  updated_at timestamptz NOT NULL,
  CHECK (reserved <= on_hand)
);

CREATE TABLE customer_order (
  order_id        bigint      PRIMARY KEY,
  tenant_id       int         NOT NULL,
  user_id         bigint      NOT NULL,
  status          text        NOT NULL CHECK (status IN ('created','paid','fulfilled','refunded','cancelled')),
  placed_at       timestamptz NOT NULL,
  currency        char(3)     NOT NULL DEFAULT 'USD',
  total_minor     bigint      NOT NULL DEFAULT 0,
  idempotency_key text,
  UNIQUE (tenant_id, idempotency_key),
  FOREIGN KEY (tenant_id, user_id) REFERENCES app_user (tenant_id, user_id)   -- tenant-safe FK
);

CREATE TABLE order_line (
  order_id         bigint NOT NULL REFERENCES customer_order,
  line_no          int    NOT NULL,
  product_id       bigint NOT NULL REFERENCES product,
  qty              int    NOT NULL CHECK (qty > 0),
  unit_price_minor int    NOT NULL CHECK (unit_price_minor >= 0),
  PRIMARY KEY (order_id, line_no)
);

CREATE TABLE payment (
  payment_id   bigint      PRIMARY KEY,
  order_id     bigint      NOT NULL REFERENCES customer_order,
  kind         text        NOT NULL CHECK (kind IN ('charge','refund')),
  amount_minor bigint      NOT NULL CHECK (amount_minor > 0),
  status       text        NOT NULL CHECK (status IN ('pending','succeeded','failed')),
  created_at   timestamptz NOT NULL
);

CREATE TABLE shipment (
  shipment_id  bigint      PRIMARY KEY,
  order_id     bigint      NOT NULL REFERENCES customer_order,
  carrier      text        NOT NULL,
  shipped_at   timestamptz NOT NULL,
  delivered_at timestamptz                                -- NULL = still in transit
);

CREATE TABLE review (
  review_id  bigint      PRIMARY KEY,
  product_id bigint      NOT NULL REFERENCES product,
  user_id    bigint      NOT NULL REFERENCES app_user,
  rating     smallint    NOT NULL CHECK (rating BETWEEN 1 AND 5),
  body       text,                                        -- NULL and '' both occur
  created_at timestamptz NOT NULL
);

CREATE TABLE event (                                      -- analytics stream (semi-structured payload)
  event_id    bigint      PRIMARY KEY,
  tenant_id   int         NOT NULL REFERENCES tenant,
  user_id     bigint,                                     -- NULL = anonymous
  event_type  text        NOT NULL,
  occurred_at timestamptz NOT NULL,
  payload     jsonb       NOT NULL DEFAULT '{}'
);

CREATE TABLE stg_import (                                 -- deliberately messy staging data
  row_id      int  PRIMARY KEY,
  email_text  text,
  signup_text text,
  amount_text text
);
