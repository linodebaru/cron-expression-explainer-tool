# cron-expression-explainer

Make sense of cron expressions without opening the man page:

```bash
python3 cron_explain.py '*/15 9-18 * * 1-5'
```

```
minute: every 15, starting at the beginning
hour: 9 through 18
day of month: every
month: every
day of week: 1-5
```

Great for auditing the scheduled jobs on a server you just inherited.
