# CS 321 - Group 3

This is the repository that hosts the racecar code for CS 321.

**Notes for WebCam stuff:**

- Increase partition size of SD card first before installing OpenCV
	- Use these commands first:
		```
		>sudo /opt/scripts/tools/grow_partition.sh
		>sudo reboot now
		```
	
	- If that doesn't work, do it manually: https://elinux.org/Beagleboard:Expanding_File_System_Partition_On_A_microSD (For "Do you want to remove the signature? [Y]es/[N]o:", type Y) 
	- You may need to mount the new partition (Use df -h to check if your partition is mounted already). https://www.simplified.guide/linux/disk-mount
		
- Get a newer SD card if possible (Video FPS is really low on older cards for some reason.. *maybe R/W speed?*)

- Ideally download all packages/ dependencies on a hotspot, Prof's Modem, or non-mason WiFi.
  - Prof's Modem WiFi SSID: 
	  - GL-A1300-97b
	-  pass: W3JZ7Q295M
  -  Connect via connmanctl
        - https://www.fis.gatech.edu/how-to-configure-bbw-wifi/

- Commands for installing OpenCV and it's dependencies:
	```
	>sudo apt-get install -y python3-dev python3-tk python3-numpy python3-pip 

	>pip3 install --upgrade pip 

	>pip3 install scikit-build

	>sudo apt-get install python-opencv
    
	>sudo apt-get install -y libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine2-dev libdigest-sha-perl

	>sudo apt-get install -y zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev libjasper-dev libopenexr-dev libgdal-dev
    
	>sudo apt-get install -y build-essential cmake vim curl software-properties-common nmap htop iftop tree
	```
- May or may not need these commands
	
		>sudo apt-get install libopencv-dev
		
		>sudo apt-get install build-essential cmake
		
		>sudo apt-get install zlib1g-dev libwebp-dev libpng-dev libjasper-dev libtiff5-dev libopenexr-dev libgdal-dev libjpeg-dev
		
		>sudo apt-get install qt5-default libvtk6-dev
		
		>sudo apt-get install libavcodec-dev libavformat-dev libdc1394-22-dev libswscale-dev libtheora-dev libxvidcore-dev libx264-dev libvorbis-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine2-dev libtbb-dev
		
- ffmpeg, ffplay, & MediaMTX
