#!/usr/bin/python
import time
import systemd.daemon

def main():
    print('Starting my python service ...')
    time.sleep(5)
    print('Startup complete')

    # Tell systemd that our service is ready
    systemd.daemon.notify('READY=1')

    running = True
    steps = 0
    while running:
        print('my python service is running (step: {})'.format(steps))
        if steps == 10:
            break
        steps += 1
        time.sleep(5)


if __name__ == '__main__':
    main()
    print('closing my python service')
