%define svn     912203
Name:           solid-actions-kcm
Version:        0.0
Summary:        Edit and add Solid actions
Release:        %mkrel 0.%svn.2
License:        GPL
Group:          Graphical desktop/KDE
URL:            http://websvn.kde.org/trunk/playground/base/solid-actions-kcm/
Source0:        %name-%version.%svn.tar.bz2
BuildRoot:      %_tmppath/%name-%version-%release-buildroot
BuildRequires:  kdelibs4-devel

%description
Edit and add Solid actions

%files
%defattr(-,root,root)
%{_kde_libdir}/kde4/kcm_solid_actions.so
%{_kde_datadir}/kde4/services/solid-actions.desktop

#-----------------------------------------------------------------------------

%prep
%setup -q -n %name

%build

%cmake_kde4

%make


%install
rm -rf %buildroot
%makeinstall_std -C build
%clean
rm -rf %{buildroot}

