+++
draft = false
date = 2018-06-05T07:22:06+02:00
title = "Unraid OS Windows 10 VM"
slug = "unraid"
tags = ["system", "linux", "kvm", "os"]
categories = ["system", "linux", "kvm", "os"]
+++

A lot of the information here come from [this guy](https://www.youtube.com/channel/UCZDfnUn74N0WeAPvMqTOrtA/featured).

He makes really good videos to explain Unraid OS concepts.

## Windows 10 VMs with GPU Passthrough

The purpose is to create a Windows 10 KVM VM with a dedicated GPU to have optimal performances.

### Stage 1: Setup the VM without any passed through hardware

##### I. Download a copy of the latest windows 10 iso

You can download the official image from [here](https://www.microsoft.com/en-us/software-download/windows10).

Copy it to a share on our Unraid system (`isos` by default)

##### II. Get a cheap Windows 10 license

You can find really cheap licenses on different marketplaces like Amazon.

##### III. Install the virtio drivers

On Unraid, in `Settings/VM Manager`, we can download the laster VirtIO driver ISO for Windows.

##### IV. Install the system

###### CPUs

Unraid is using the first vCPUs (first `CPU 0`) for computing, it is better to let them free.

When assigning `Logical CPUs` (threads) to a VM, it is best practice to make sure we are assigning both hyperheaded pairs of each core.

###### RAM

Always make sure we have enough `RAM` for our server as well as the VM.

For Windows 10, we need at least `2GB`.

To be safe, `8GB` should be fine.

###### BIOS

Leave the `BIOS` set as `OVMF` unless we can't install the OS with this setting.

If passing through a GPU, the GPU must support EFI boot to use `OVMF`.

If we know our GPU doesn't support EFI, then use `SEABIOS`.

###### Hyper V

`Hyper V` should be set to `Yes`.

###### OS Install

The `OS Install ISO` should be set to our Windows 10 ISO's location.

`OS Install CDRom Bus` should be set to `IDE`.

######  VirtIO Driver

`VirtIO Driver ISO` should be set to the location of the VirtIO driver we have downloaded.

`VirtIO Driver CDRom Bus` should be set to `IDE`.

###### VDisks

We don't need a large vDisk, we will store most of the data on the array using mapped drives and symlinks.

###### Installation

When we need to choose a disk to install Windows, we will see no disk appearing in the list.

To see the vDisk, we need to install a driver.

Click on `Load driver` and `Browse`.

Select the `virtio-win CD Drive/viostor/w10/amd64` and click on next.

We will be able to see the vDisk and complete the installation.

##### V. Post install tasks

###### VirtIO Drivers

Go to the `Device Manager`, we will see 3 devices that don't have a driver in `Other Devices`.

The `Display Adapter` is a driver to install as well.

Click on `Update Driver` and `Browse my computer for driver software`.

Look for the location of our `VirtIO CDRom` and `next` to install the driver.

Repeat the operation for each missing driver.

###### Softwares

We can download a bunch of packages in the same time thanks to some services like [ninite](https://ninite.com/).

We can disable windows 10 phoning home with our data by install a tool like [Windows Privacy Tweaker](https://www.phrozen.io/freeware/windows-privacy-tweaker/).

##### VI. Remote connection to the VM

VLC is used by default on Unraid. It is not the most performant one.

Using one like [splashtop](https://www.splashtop.com/) or [teamviewer](https://www.teamviewer.com/en/) will considerably improve the perfomances.

To have remote distance feature with splashtop using a free account, we just need to set a vpn router from our server to access it locally.

##### VII. How to use symlinks to make efficient

##### VIII. Install a virtual sound card

### Stage 2: Passthrough the hardware needed

##### I. Essentials checks before attempting passthrough

##### II. Passing through the GPU

##### III. Passing through the sound

##### IV. Passing through keyboard and other usb devices

##### V. Installing GPU drivers

##### VI. Enabling MSI interrupts to stop sound problems

##### VII. Installing games
