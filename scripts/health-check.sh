#!/bin/bash
# Simple health check script

LOG_FILE="logs/health_check_$(date +%Y%m%d).log"

echo "--- System Health Check: $(date) ---" >> $LOG_FILE
echo "Disk Usage:" >> $LOG_FILE
df -h | grep '/$' >> $LOG_FILE
echo "" >> $LOG_FILE

echo "Memory Usage:" >> $LOG_FILE
free -h | grep 'Mem:' >> $LOG_FILE
echo "-----------------------------------" >> $LOG_FILE
