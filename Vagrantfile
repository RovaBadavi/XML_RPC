Vagrant.configure("2") do |config|
  # Shared folder between host and VM
  config.vm.synced_folder ".", "/vagrant"

  # VirtualBox settings (applies to all VMs)
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.cpus = 1
  end

  config.vm.define "ServerVM" do |host1|
    host1.vm.box = "ubuntu/focal64"
    host1.vm.hostname = "ServerVM"
    host1.vm.network "private_network", ip: "192.168.56.10"
  end
end