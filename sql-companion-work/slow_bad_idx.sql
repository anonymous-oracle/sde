SELECT u.user_id,
       (SELECT count(*) FROM work.ev e
         WHERE e.user_id = u.user_id AND e.event_type = 'page_view'
           AND e.occurred_at <  (SELECT min(p.occurred_at) FROM work.ev p WHERE p.user_id = u.user_id AND p.event_type = 'purchase')
           AND e.occurred_at >= (SELECT min(p.occurred_at) FROM work.ev p WHERE p.user_id = u.user_id AND p.event_type = 'purchase') - interval '24 hours') AS views_24h
FROM lab.app_user u
WHERE EXISTS (SELECT 1 FROM work.ev p WHERE p.user_id = u.user_id AND p.event_type = 'purchase')
