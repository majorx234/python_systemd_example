import time
from pystemd.systemd1 import Unit
from pystemd.dbuslib import DBus


def main():
    with DBus(user_mode=True) as bus:
        unit = Unit(b"my_python_service.service", bus=bus)
        unit.load()

        running = True
        is_my_pathon_service_alive = False
        while running:
            if unit.Unit.ActiveState == b'active':
                print("my python service is active")
                if unit.Unit.SubState == b'running':
                    is_my_pathon_service_alive = True
                    unit.Service.GetProcesses()
                    pid = unit.Service.MainPID
                    print("my python service is alive with PID:{}".format(pid))

                else:
                    print("my python service not running yet")
            else:  # inactive
                print("my python service is dead -> reanimating")
                unit.Unit.Start(b'replace')
            time.sleep(5)


if __name__ == "__main__":
    main()
