#!/bin/bash
# Automated Backup and Cleanup Script

BACKUP_DIR="/var/backups/project3"
SOURCE_DIR="/home/dele/LAMP-Stack-Ops-Automation"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
RETENTION_DAYS=7

# 1. Create backup directory if it doesn't exist
mkdir -p $BACKUP_DIR

# 2. Create compressed archive backup
tar -czf $BACKUP_DIR/project3_backup_$TIMESTAMP.tar.gz $SOURCE_DIR

# 3. Clean up backups older than retention period
find $BACKUP_DIR -type f -name "*.tar.gz" -mtime +$RETENTION_DAYS -delete

echo "Backup completed and files older than $RETENTION_DAYS days cleaned."
