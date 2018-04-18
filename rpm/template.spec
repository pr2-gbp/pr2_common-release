Name:           ros-kinetic-pr2-msgs
Version:        1.12.2
Release:        0%{?dist}
Summary:        ROS pr2_msgs package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_msgs
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-std-msgs

%description
Messages for representing PR2 state, such as battery information and the PR2
fingertip sensors.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Apr 18 2018 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 1.12.2-0
- Autogenerated by Bloom

* Tue Feb 13 2018 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 1.12.1-0
- Autogenerated by Bloom

* Fri Apr 22 2016 Austin Hendrix <ahendrix@willowgarage.com> - 1.12.0-0
- Autogenerated by Bloom

