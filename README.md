# Info
- example of a python file running as a sysdemd service
  - uses: https://github.com/systemd/python-systemd
  - to signal systemd that it is running
- have a second script who could start/stop this service
  - uses python lib provided by systemd maintainers: https://github.com/systemd/pystemd
  - WIP

# usage:
- copy service:
  - ```cp service/my_python_service.service ~/.config/systemd/user```
- start service:
  - ```systemctl --user start my_python_service.service```
- check status:
  - ```systemctl --user status my_python_service.service```
## loging
- ```journalctl --user-unit my_python_service.service```
