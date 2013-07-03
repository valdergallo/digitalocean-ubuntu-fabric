digitalocean-ubuntu-fabric
==========================

Fabric colection to deploy Django with nginx and gunicorn in Digital Ocean

--------------------------
Available commands:

    command                        Send custom command with args or not. Usag...
    create_package                 Create virtualenv
    create_www                     Configure permissions on www
    dbshell                        Django DB Shell
    deploy                         Update git repository and reset nginx
    df                             Partition info
    free                           Show free memory
    info                           Show host name
    load_requirements              Install requirements packages
    migrate                        Django Syncdb
    nginx                          Run service command to nginx
    nginx_config                   Send nginx configuration
    nginx_disable_site             Disable nginx site
    nginx_enable_all_site          Enable all sites
    nginx_enable_site              Enable nginx site
    nginx_reset                    Reset nginx
    nginx_start                    Start nginx
    nginx_stop                     Stop nginx
    omo                            Lava mais branco
    pip                            Install package on server. Usage: pip:inst...
    py                             Execute python command
    service                        Control Services. Usage:start,nginx
    setup                          Install default packages for django
    setup_webserver                Instal default packages for django and NGI...
    shell                          Django Shell
    static                         Collect Static Files
    supervisor                     Send supervisor command
    supervisor_config              Send all supervisors configurations
    supervisor_disable_site        Disable supervisor site
    supervisor_reload              Reload supervisor config files
    supervisor_reset               Reset supervisor
    supervisor_reset_gunicorn      Reset gunicorn
    supervisor_start               Start supervisor
    supervisor_stop                Stop supervisor
    supervisor_upload_file_config  Send supervisor configuration
    swap                           List swap
    swapon                         Add a Swap File
    syncdb                         South Migration
    update                         Update server content
    virtualenv                     Activate virtualenv
