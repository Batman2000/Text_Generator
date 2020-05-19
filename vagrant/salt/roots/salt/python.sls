numpy:
  pip3.installed:
    - name: numpy
    - bin_env: '/usr/bin/pip3'
    - require:
      - pkg: python3-pip
