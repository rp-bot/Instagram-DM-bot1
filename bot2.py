import notification_alert as notif
import reply

if __name__ == '__main__':
    away = True
    while away:
        notif.checkstatus()
        reply.bot_init()
