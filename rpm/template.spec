Name:           ros-indigo-pr2-dashboard-aggregator
Version:        1.11.14
Release:        1%{?dist}
Summary:        ROS pr2_dashboard_aggregator package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_dashboard_aggregator
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-pr2-msgs
Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin

%description
A simple script that aggregates all of the topics that a
&quot;pr2_dashboard&quot; app might be interested in.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Feb 22 2016 Devon Ash <dash@clearpathrobotics.com> - 1.11.14-1
- Autogenerated by Bloom

* Mon Feb 22 2016 Devon Ash <dash@clearpathrobotics.com> - 1.11.14-0
- Autogenerated by Bloom

* Mon Feb 08 2016 Devon Ash <dash@clearpathrobotics.com> - 1.11.13-0
- Autogenerated by Bloom

* Thu Feb 04 2016 Devon Ash <dash@clearpathrobotics.com> - 1.11.12-0
- Autogenerated by Bloom

* Fri Jan 22 2016 Devon Ash <dash@clearpathrobotics.com> - 1.11.11-0
- Autogenerated by Bloom

* Fri Dec 04 2015 Devon Ash <dash@clearpathrobotics.com> - 1.11.10-0
- Autogenerated by Bloom

* Tue Feb 10 2015 Devon Ash <dash@clearpathrobotics.com> - 1.11.9-0
- Autogenerated by Bloom

* Tue Jan 13 2015 Devon Ash <dash@clearpathrobotics.com> - 1.11.8-0
- Autogenerated by Bloom

