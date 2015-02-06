%define git 1
%define gitdate %(date +%Y%m%d)

%define major 0
%define libname %mklibname polkitkdekcmodulesprivate %{major}

Name:            polkit-kde-kcmodules-1
Summary:         PolicyKit KDE Configuration
Group:           Graphical desktop/KDE
Version:         1.0.0
Release:         0.4
License:         GPL
URL:             https://projects.kde.org/projects/extragear/base/%{name}
# http://anongit.kde.org/polkit-kde-kcmodules-1/polkit-kde-kcmodules-1-latest.tar.gz
Source0:         %{name}%{?!git:-%{version}}.tar.xz
BuildRequires:   polkit-qt-1-devel >= 0.98.1
BuildRequires:   kdelibs4-devel
Requires:        %{libname} = %{version}-%{release}

%description
From this module, you can configure PolicyKit action policies,
system administrators and priorities for this configuration

%files
%{_sysconfdir}/dbus-1/system.d/org.kde.polkitkde1.helper.conf
%{_kde_libdir}/kde4/kcm_polkitactions.so
%{_kde_libdir}/kde4/kcm_polkitconfig.so
%{_kde_libdir}/kde4/libexec/polkitkde1helper
%{_datadir}/dbus-1/system-services/org.kde.polkitkde1.helper.service
%{_kde_datadir}/kde4/services/kcm_polkitactions.desktop
%{_kde_datadir}/kde4/services/kcm_polkitconfig.desktop
%{_kde_datadir}/kde4/services/settings-system-policies.desktop
%{_datadir}/polkit-1/actions/org.kde.polkitkde1.policy

#--------------------------------------------------------------------

%package -n %{libname}
Summary:         KDE 4 core library
Group:           System/Libraries

%description -n %{libname}
KDE 4 core library.

%files -n %{libname}
%{_kde_libdir}/libpolkitkdekcmodulesprivate.so.%{major}*

#--------------------------------------------------------------------

%package devel
Summary:         Polkit KDE Modules Development
Group:           Development/KDE and Qt
Requires:        kdelibs4-devel
Requires:        %{libname} = %{version}-%{release}

%description devel
Development files for polkit-kde-kcmodules-1.

%files devel
%{_kde_libdir}/libpolkitkdekcmodulesprivate.so

#--------------------------------------------------------------------

%prep
%setup -q%{?git:n %{name}}

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build


