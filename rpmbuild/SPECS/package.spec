%define unmangled_name proton-vpn-gtk-app
%define version 0.13.2
%define logo_filename proton-vpn-logo.svg
%define desktop_entry_filename protonvpn-app.desktop
%define release 1

Prefix: %{_prefix}
Name: %{unmangled_name}
Version: %{version}
Release: %{release}%{?dist}
Summary: %{unmangled_name} library

Group: ProtonVPN
License: GPLv3
Vendor: Proton Technologies AG <opensource@proton.me>
URL: https://github.com/ProtonVPN/%{unmangled_name}
Source0: %{unmangled_name}-%{version}.tar.gz
Source3: %{desktop_entry_filename}
Source4: %{logo_filename}
BuildArch: noarch
BuildRoot: %{_tmppath}/%{unmangled_name}-%{version}-%{release}-buildroot

BuildRequires: gtk3
BuildRequires: desktop-file-utils
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-gobject
BuildRequires: python3-proton-vpn-api-core
BuildRequires: python3-proton-vpn-logger
BuildRequires: python3-proton-vpn-network-manager-openvpn
BuildRequires: python3-proton-keyring-linux-secretservice
BuildRequires: python3-dbus

Requires: gtk3
Requires: python3-gobject
Requires: python3-proton-vpn-api-core
Requires: python3-proton-vpn-logger
Requires: python3-proton-vpn-network-manager-openvpn
Requires: python3-proton-keyring-linux-secretservice
Requires: python3-dbus

%{?python_disable_dependency_generator}

%description
Package %{unmangled_name}.


%prep
%setup -n %{unmangled_name}-%{version} -n %{unmangled_name}-%{version}

%build
python3 setup.py build

%install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE3}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{desktop_entry_filename}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
cp %{SOURCE4} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{logo_filename}
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES


%files -f INSTALLED_FILES
%{python3_sitelib}/proton/
%{python3_sitelib}/proton_vpn_gtk_app-%{version}*.egg-info/
%{_datadir}/applications/%{desktop_entry_filename}
%{_datadir}/icons/hicolor/scalable/apps/%{logo_filename}
%defattr(-,root,root)

%changelog
* wo feb 08 2023 Josep Llaneras <josep.llaneras@proton.ch> 0.13.2
- Fix random reconnection issues

* Tue Feb 07 2023 Josep Llaneras <josep.llaneras@proton.ch> 0.13.1
- Fix several search issues

* Tue Feb 07 2023 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.13.0
- Move logout to menu and refactor code

* Mon Feb 06 2023 Josep Llaneras <josep.llaneras@proton.ch> 0.12.0
- Add search bar

* Thu Feb 02 2023 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.11.2
- Fix app icon for Wayland

* Mon Jan 30 2023 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.11.1
- Fix bug report dialog as per customer support guidelines

* Mon Jan 30 2023 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.11.0
- Feature: About dialog

* Thu Jan 26 2023 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.10.4
- Display pop-up when unable to reach API during logout

* Thu Jan 26 2023 Josep Llaneras <josep.llaneras@proton.ch> 0.10.3
- Add window icon

* Mon Jan 23 2023 Josep Llaneras <josep.llaneras@proton.ch> 0.10.2
- Submit bug report using proton-core

* Mon Jan 23 2023 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.10.1
- Fix: Bug report feature

* Tue Jan 17 2023 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.10.0
- Feature: Add issue report submission dialog

* Fri Jan 13 2023 Josep Llaneras <josep.llaneras@proton.ch> 0.9.5
- Load VPN server details from persisted connection

* Wed Jan 11 2023 Josep Llaneras <josep.llaneras@proton.ch> 0.9.4
- Fix Fail silently when the server list or the client config could not be updated

* Fri Jan 06 2023 Josep Llaneras <josep.llaneras@proton.ch> 0.9.3
- Fix quick connect widget glitch when opening the app twice

* Thu Dec 29 2022 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.9.2
- Attempt to reconnect after user session has been unlocked from suspend

* Thu Dec 22 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.9.1
- Do not show popups on connection errors

* Tue Dec 20 2022 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.9.0
- Add unit tests and improve API data handling

* Wed Dec 14 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.8.0
- Reconnect to VPN when network connectivity is detected

* Tue Dec 06 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.7.2
- Fix app crash after starting the app with a persisted connection

* Tue Dec 06 2022 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.7.1
- Fix issue where current connection was not properly being detected

* Mon Dec 05 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.7.0
- Get server name/id from connection status update

* Fri Dec 02 2022 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.6.6
- Check if the current connection is active before disconnecting

* Tue Nov 15 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.6.5
- Check if the current connection is active before disconnecting

* Mon Nov 14 2022 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.6.4
- Display error dialog whenever a connection fails to be established

* Fri Nov 11 2022 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.6.3
- Add Proton VPN logging library

* Fri Nov 7 2022 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.6.2
- Ensure that vpn connection is stopped before logging out the user, if there is one

* Fri Nov 4 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.6.1
- Fix bug happening when connecting to a server without disconnecting first from the previous one

* Mon Oct 31 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.6.0
- Show the login screen when the session expired

* Tue Oct 04 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.5.1
- Fix several bugs in the server list widget

* Wed Sep 28 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.5.0
- Add "Connect" button on country rows

* Mon Sep 26 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.4.1
- Cleanup server list after logout

* Fri Sep 23 2022 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.4.0
- Properly implement Quick Connect

* Fri Sep 23 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.3.1
- Fix crash when connecting to free server

* Thu Sep 22 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.3.0
- Display upgrade button for servers that require a higher tier plan to connect to

* Wed Sep 21 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.2.0
- Group servers by country

* Mon Sep 19 2022 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.1.2
- Add basic logging

* Mon Sep 19 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.1.1
- Fix app freeze when disconnecting from VPN

* Thu Sep 15 2022 Josep Llaneras <josep.llaneras@proton.ch> 0.1.0
- Allow the user to connect to a concrete VPN server

* Mon Jun 4 2022 Alexandru Cheltuitor <alexandru.cheltuitor@proton.ch> 0.0.2
- First RPM release
