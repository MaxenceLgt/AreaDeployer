<div style="text-align:center">
  <img src="https://github.com/user-attachments/assets/f92370ae-196c-437a-8437-972641222206" width="400" alt="logo"/>
</div>

# Build & Run the Project

## Prerequisites

To build and start the deployer, you will need an Azure virtual machine with the following specifications:

- **Operating System:** Debian 12 Bookworm  
- **Network Access:** SSH, HTTPS, and HTTP

For detailed documentation on prerequisites and instructions for building the virtual machine, refer to the [complete guide](https://github.com/MaxenceLgt/AreaDeployer/wiki).

Additionally, you will need `ansible-playbook` to install the automatic deployment configuration. Ensure that `ansible-playbook` is installed on your machine before proceeding.


### Ansible Playbook Installation on Linux

You can install `ansible-playbook` using the following command:
```sh
sudo apt update
sudo apt install ansible ansible-core
```

### Ansible Playbook Installation on Windows

Since Ansible is not natively available on Windows operating systems, you must run the project from an operating system that supports Ansible installation. For more information, refer to the [official documentation](https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html#installing-ansible-on-windows).

## Run the Project

### VM Setup Information  

To deploy the entire CI/CD pipeline on your VM, you need to provide some mandatory information for Ansible in the `ansible/production.yml` file:  

- **ansible_host**: The public IP address of your VM.  
- **ansible_port**: The SSH connection port (default is 22).  
- **ansible_ssh_user**: The username created during the VM setup.  
- **ansible_ssh_private_key_file**: The path to your private SSH key file.

### Preparing Files for Deployment  

Depending on how your application works and how it needs to be started, you may need to create specific files to copy to the VM (e.g., environment files, Nginx configuration, etc.).  

For more details, refer to the [Project Configuration Guide](https://github.com/MaxenceLgt/AreaDeployer/wiki).  

### Running the Ansible Playbook  

Once the CICD setup and all required application files are prepared for deployment on your Ansible-configured VM, execute the following command:  

```sh  
ansible-playbook -i ansible/production.yml ansible/playbook.yml  
```  

If you need to deploy or redeploy a specific task, such as the Flask server, include the `--tags` flag in your command:  

```sh  
ansible-playbook -i ansible/production.yml ansible/playbook.yml --tags #tag (e.g., hooks)  
```

### Global Documentation

The complete documentation for the project is available on the [project wiki](https://github.com/MaxenceLgt/AreaDeployer/wiki).

## Cheat Warning

This repository is public for several reasons. As it is part of a third-year school project at EPITECH, please refrain from using it for your own EPITECH projects to avoid being flagged for cheating (-42). I am not responsible for any misuse of my repository.

## Author

<table>
    <tbody>
        <tr>
            <td align="center">
                <a href="https://github.com/MaxenceLgt">
                    <img src="https://avatars.githubusercontent.com/u/114743051?v=4" width="100px;" alt="MaxenceLgt"/><br />
                    <sub><b>MaxenceLgt</b></sub>
                </a>
            </td>
        </tr>
    </tbody>
</table>
