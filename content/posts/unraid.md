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

---

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

###### Setup Windows Initialization

Setup Up Region, Keyboard Layout, Netowrk (to skip), User Settings, Cortana and Privacy Settings during the initialization.

###### VirtIO Drivers

Go to the `Device Manager`, we will see 3 devices that don't have a driver in `Other Devices`.

The `Display Adapter` is a driver to install as well.

Click on `Update Driver` and `Browse my computer for driver software`.

Look for the location of our `VirtIO CDRom` and `next` to install the driver.

Repeat the operation for each missing driver.

###### guest-agent install

Go to `virtio-win` drive and install `gpu-agent/qemu-ga-x64.msi`.

###### Video Settings

We can now change the video resolution going in `Display Settings`.

###### Softwares

We can download a bunch of packages in the same time thanks to some services like [ninite](https://ninite.com/).

We can disable windows 10 phoning home with our data by install a tool like [Windows Privacy Tweaker](https://www.phrozen.io/freeware/windows-privacy-tweaker/).



##### VI. Remote connection to the VM

VLC is used by default on Unraid. It is not the most performant one.

Using one like [splashtop](https://www.splashtop.com/) or [teamviewer](https://www.teamviewer.com/en/) will considerably improve the perfomances.

To have remote distance feature with splashtop using a free account, we just need to set a vpn router from our server to access it locally.

##### Pimp Settings

We need to change some windows settings for a better VM experience.

###### Power Options

In `Choose what the power button does` disable `Turn on fast startup`.
In `Choose or customize a power plan` click on `High performance`,
then go to `Change plan settings` and disable `Hard disk/Turn off hard disk afer` and `USB settings/USB selective suspend setting/Setting`.
When done, you can disable `Turn off the display` as well.

###### Disable indexing

It is useful to reduce unnecessary IO on the vdisk.
Go to `services.msc` and stop `Windows Search` service and disable it from its properties.

Run `cmd` as administrator and enter `powercfg -h off`.
To disable disk fragmentation, go to the local disk properties and `tools/optimize`.
Then go to change settings and untick `Run on a schedule`.

##### VII. How to use symlinks to make efficient

Create a share with SMB enable.
Map a network drive and relocate document folder.
If you cannot find it in Windows tap your server address `\\[ip]\` in file explorer.
Modify the related symlink (`Downloads` for example).

##### VIII. Install a virtual sound card

You need to modify the VM `xml` under the video tag at the bottom of the file:
```
<sound model='ich9'>
</sound>
```

---

### Stage 2: Passthrough the hardware needed

##### I. Essentials checks before attempting passthrough

###### 1. CPU/Motherboard must support IOMMU

Intel's implementation of IOMMU is known as VT-d.
AMD's implementation of IOMMU is known as AMD-Vi.

###### 2. IOMMU group

Any hardware that is passed through needs to be in its own IOMMU group it can't share a group
with other hardware (unless that is also going to be passed through at the same time).
If a device is in a group with devices that we don't want to pass through, we need to set 
`Enable PCIe ACS Override` in `Settings/VM Manager` and reboot the system.

##### II. Passing through the GPU

##### III. Passing through the sound

##### IV. Fixing demonic sound

##### V. Three common GPU passthrough problems and how to solve them

##### VI. Making non EFI compatible GPU EFI compatible

##### VII. Passing through a USB controller
