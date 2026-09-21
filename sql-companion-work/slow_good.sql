WITH fp AS (SELECT user_id, min(occurred_at) AS t FROM lab.event WHERE event_type = 'purchase' AND user_id IS NOT NULL GROUP BY user_id)
SELECT fp.user_id, count(e.event_id) AS views_24h
FROM fp LEFT JOIN lab.event e
  ON e.user_id = fp.user_id AND e.event_type = 'page_view' AND e.occurred_at < fp.t AND e.occurred_at >= fp.t - interval '24 hours'
GROUP BY fp.user_id
