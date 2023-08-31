Vagrant.configure("2") do |config|
    servers=[
        {
            :hostname => "controller",
            :box => "bento/ubuntu-18.04",
            :ip => "192.168.56.10",
            :ssh_port => "2200"
        },
        {
            :hostname => "node1",
            :box => "bento/ubuntu-18.04",
            :ip => "192.168.56.11",
            :ssh_port => "2201"
        },
        {
            :hostname => "node2",
            :box => "bento/ubuntu-18.04",
            :ip => "192.168.56.12",
            :ssh_port => "2202"
        },
        {
            :hostname => "node3",
            :box => "bento/ubuntu-18.04",
            :ip => "192.168.56.13",
            :ssh_port => "2203"
        }
    ]

    servers.each do |machine|
        config.vm.define machine[:hostname] do |server|
            server.vm.box = machine[:box]
            server.vm.hostname = machine[:hostname]
            server.vm.network :private_network, ip: machine[:ip]
            server.vm.network "forwarded_port", guest: 22, host: machine[:ssh_port], id: "ssh"
            server.ssh.forward_agent = true
            server.vm.provider :virtualbox do |vb|
                vb.customize ["modifyvm", :id, "--memory", 512]
                vb.customize ["modifyvm", :id, "--cpus", 1]
                vb.customize ["modifyvm", :id, "--cableconnected1", "on"]
            end
        end
    end
end






