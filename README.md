Project 3: Automation & Monitoring

## 1: System Health Check and Cron Job

Automated system health checks monitors disk and Memory usage via a shell script and scheduled execution using `cron` to maintain system awareness. [View Output in docs/task1-output.txt]


## 2: Automated Backup and Cleanup

A daily backup script (scripts/backup-clean.sh) archives the project directory to /var/backups using tar and automatically deletes backups older than 7 days. The task includes creating the script, adjusting paths, setting execution permissions, testing the script, verifying backup creation in /var/backups, and scheduling daily execution via a cron job.

[View Output in docs/task2-output.txt]


## 3: Configuration Management with Ansible

Ansible playbooks were created and executed to automatically provision the full LAMP stack (Apache, MariaDB, PHP) and deploy a test application file. [View Output in docs/task3-output.txt]


## 4: Advanced Monitoring and Alerting

A Python script was implemented to perform application-level health checks (verifying the web server and content) and utilize `notify-send` to deliver critical desktop alerts upon failure. [View Output in docs/task4-output.txt]
