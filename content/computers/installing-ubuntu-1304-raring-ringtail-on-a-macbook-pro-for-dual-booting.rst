Installing Ubuntu 13.04 Raring Ringtail on a MacBook Pro for Dual Booting
#########################################################################
:date: 2013-05-22 06:06
:author: Kyle Barlow (noreply@blogger.com)
:tags: ubuntu
:slug: installing-ubuntu-1304-raring-ringtail-on-a-macbook-pro-for-dual-booting

I recently installed Ubuntu onto my MacBook alongside OSX for dual
booting, and learned a few lessons throughout the process. Below are the
steps that I took. I have a MacBookPro 8,1 but these instructions might
be applicable to other models as well. Be sure to also read
the\ `"official" Ubuntu installation
guide <https://help.ubuntu.com/community/MacBookPro>`__. I also found `a
post by James
Jesudason <http://randomtutor.blogspot.com/2013/02/installing-ubuntu-1304-on-retina.html>`__
to be helpful.

These instructions are fairly sparse, but should help point you in the
right direction if you are less experienced with any of the steps.

#. Reduce partition size in the OSX "disk utility" tool. I dragged the
   partition size until I had enough free space left on the disk for my
   Ubuntu partition (I wanted 50gb but less should be ok). This took
   several hours.
#. Install the \ `rEFInd boot
   manager <http://www.rodsbooks.com/refind/>`__. I downloaded the most
   recent binary file (0.6.11) and ran install.sh, which worked without
   any other options. rEFInd was installed into the /EFI on my root
   filesystem.
#. Install the `ext4
   driver <http://www.rodsbooks.com/refind/drivers.html>`__ in rEFInd.
   The driver is packaged with the binaries, but must be copied into
   /EFI/refind/drivers in order to be active. I had to create the
   drivers directory in /EFI with "sudo mkdir /EFI/refind/drivers" as it
   did not already exist. I then copied (as root) "ext4\_x64.efi"
   from refind-bin-0.6.11/refind/drivers\_x64 into the newly created
   drivers directory.
#. Load the Ubuntu installer CD (must be the special Mac `version of
   Ubuntu <http://releases.ubuntu.com/raring/>`__ - labeled on that page
   as "64-bit Mac (AMD64) desktop image"). Instead of choosing to
   install Ubuntu, choose to try it out instead. Open up a terminal and
   run "ubiquity -b" and then proceed with the installation. Running
   with the -b flag tells Ubuntu not to install a bootloader, which
   won't be necessary as rEFInd can boot a kernel directly. During the
   install process, the default option should be to install in the disk
   free space, but you should verify this. I chose to manually create an
   ext4 partition for my root mount point and a 2gb swap partition
   instead of using the automatic option.
#. After the installation finishes, select the option to continue to try
   Ubuntu. In the terminal, run something like "sudo blkid /dev/sda\*".
   Look for the UUID corresponding to your Ubuntu root mount point.
#. With Ubuntu still loaded off the LiveCD, find the /boot partition in
   your new install. This should probably be mounted somewhere in
   /media. In /media/.../boot, create a file called refind\_linux.conf.
   Save the below options (from the `rEFInd
   documentation <http://www.rodsbooks.com/refind/linux.html>`__),
   replacing the UUID with the one you noted in the last step
   corresponding to your Ubuntu install, into this
   file:

   .. code-block:: bash

      "Boot with standard options" "root=/dev/sda3 ro quiet splash vt.handoff=7"
      "Boot to single-user mode"   "root=UUID=1cd95082-bce0-494c-a290-d2e642dd82b7 ro single"
      "Boot with minimal options"  "root=UUID=1cd95082-bce0-494c-a290-d2e642dd82b7 ro"

#. When you restart, Ubuntu should automatically be detected and
   available to use in the rEFInd boot menu. You can make it the default
   boot option by setting default\_selection in /EFI/refind/refind.conf
   accordingly

I modified these steps slightly from the ones that I took, so let
me know in the comments if you run into any problems. Hope this helps!

