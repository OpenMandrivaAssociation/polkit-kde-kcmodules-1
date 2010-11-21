%define         git  e1e84d4d

Name:           polkit-kde-kcmodules-1
Version:        1.0.0
Summary:        PolicyKit configuration GUI for KDE
Release:        %mkrel %{?git:0.}2
License:        GPL
Group:          Graphical desktop/KDE
URL:            https://projects.kde.org/projects/extragear/base/%{name}
# For now: git archive --prefix polkit-kde-kcmodules-1/ %{git}
Source0:        %{name}-%{version}%{?git:-g%{git}}.tar.bz2
BuildRoot:      %_tmppath/%name-%version-%release-buildroot
BuildRequires:  polkit-qt-1-devel >= 0.98.1
BUildRequires:  kdelibs4-devel

%description
From this module, you can configure PolicyKit action policies,
system administrators and priorities for this configuration

%files
%defattr(-,root,root)
%{_datadir}/dbus-1/system-services/org.kde.polkitkde1.helper.service
%{_datadir}/polkit-1/actions/org.kde.polkitkde1.policy
%{_sysconfdir}/dbus-1/system.d/org.kde.polkitkde1.helper.conf
%{_kde_libdir}/kde4/kcm_polkitactions.so
%{_kde_libdir}/kde4/kcm_polkitconfig.so
%{_kde_libdir}/kde4/libexec/polkitkde1helper
%{_kde_services}/kcm_polkitactions.desktop
%{_kde_services}/kcm_polkitconfig.desktop
%{_kde_services}/settings-system-policies.desktop

#-----------------------------------------------------------------------------

%prep
%setup -q -n %name

%build

%cmake_qt4
%make


%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %{buildroot}

