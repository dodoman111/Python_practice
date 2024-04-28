SELECT
    user,
    age,
    email,
    pass,
    CASE
        WHEN user = 'ab' THEN 1
        ELSE 0
    END AS email_no
FROM
    db.users
    LEFT JOIN db.info ON db.info.user_id = db.info.user
WHERE
    TRUE
    AND user_id = "123"
ORDER BY
    user DESC