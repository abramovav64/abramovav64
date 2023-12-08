%define _destdir %_datadir/PolicyDefinitions

Name: admx-basealt
Version: 0.1.13.2
Release: alt1

Summary: BaseALT-specific ADMX policy templates
License: AGPLv3+
Group: System/Configuration/Other
Url: https://github.com/altlinux/admx-basealt
BuildArch: noarch

BuildRequires: admx-lint

Source0: %name-%version.tar

%description
BaseALT-specific ADMX files, which are registry-based policy settings provide
an XML-based structure for defining the display of the Administrative Template
policy settings in the Group Policy Object Editor.

%prep
%setup -q

%install
mkdir -p %buildroot%_destdir
cp -r ru-RU/ en-US/ BaseALT*.admx %buildroot%_destdir/

%check
for file in *.admx *-*/*.adml; do
    admx-lint --input_file "$file"
done

%files
%dir %_destdir
%_destdir

%changelog
* Tue Oct 31 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.13.2-alt1
- Edited description of blocking
- Edited English version of adml GSettings
- Fixed bugs in ModemManager policies

* Thu Oct 19 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.13.1-alt1
- Polkit-restrictions of ModemManager1 in admx-templates
- Fix polkit translate in russian language
- Fix bugs (closes: 47973, 47985, 47987, 47743, 47990, 47818, 48002)

* Tue Sep 19 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.13.0-alt1
- Added a section for user and machine policies to configure
  the graphical environment of KDE Plasma
- Added KDE Applier Enable policy
- Fix supportedOn defenitions to use ranges instead of references
- Added closure policy in admx-basealt

* Thu Jun 15 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.12.6-alt1
- Added new admx-files for polkit-actions to NetworkManager and pcsc_lite

* Thu May 11 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.12.5-alt1
- Fix typos in PolKit adml files
- Fixed descriptions for samba usershares policies

* Mon Apr 03 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.12.4-alt1
- Fix typos in adml files (closes: 42365)
- Changed policy definition to "Mechanism for copying files"
- Fixed policy "General mount policy".

* Thu Mar 09 2023 Evgeny Sinelnikov <sin@altlinux.org> 0.1.12.3-alt1
- Fix typos in adml files (closes: 42355, 42365, 42358).

* Fri Mar 03 2023 Valery Sinelnikov <greh@altlinux.org> 0.1.12.2-alt1
- Added new admx for samba usershare controls
- Added new group policies for PackageKit polkit actions
- Added new group policies for Udisks2 polkit actions
- Add machine policies for drive maps
- Added file copy mechanism configuration policy

* Thu Dec 29 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.1.12.1-alt1
- Add user policies for drive maps symlinks in home directory.
- Add warning when disabling network manager.
- Fix correction of option name open ldap tls connections in russian.
- Fix typo in cups.service

* Tue Dec 13 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.1.12-alt1
- Add control for Yandex Browser group policies mechanism.
- Improve group policies mechanisms display names and help descriptions.

* Mon Oct 24 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.1.11.2-alt1
- Fix en_US adml for script execution module for users policy.

* Wed Sep 07 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.1.11.1-alt1
- Fix machine part of file-copy group policy engine.

* Fri Aug 26 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.1.11-alt1
- Fix ability to block a disabled Mate policies.
- Fix error loading templates in gpedit.
- Add file-copy, ini-files and script policies gpupdate engines.
- Add ScrollSysvolDC policy.

* Wed Mar 02 2022 Evgeny Sinelnikov <sin@altlinux.org> 0.1.10-alt1
- Correct adml definitions for controls and group policies.
- Update machine and user packages settings.
- Add Gsettings for windows manager Marco.
- Add policies for local users support.
- Add Simply Linux 10 as BaseALT product.

* Fri Oct 22 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.9-alt1
- Fixed typo in screensaver setting in Russian translations
- Improve English translation of gsettings strings
- Fix authetication method bug for gsetting oprtion:
  org.gnome.Vino.authentication-methods

* Mon Oct 04 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.8-alt1
- Fix typos in Russian translations

* Mon Sep 20 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.7-alt1
- Added remote settings category and Vino settngs:
 + authentication-methods and vnc-password;
 + use-alternative-port and alternative-port;
 + view-only, prompt-enabled, icon-visibility and enabled.

* Sun Sep 12 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.6-alt1
- Added new categories and policies for Mate settings:
 + background;
 + screensaver;
 + user restrictions.

* Sun Jul 18 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.5-alt1
- Add new categories and policies:
 + SSHD and Systemd categories
 + Windows policies mapping support (applied for GSettings only yet)
- Add admx and adml files checking via admx-lint

* Tue Mar 23 2021 Evgeny Sinelnikov <sin@altlinux.org> 0.1.4-alt1
- Add sssd controls in separate category

* Sat Sep 12 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.1.3-alt1
- Add sshd-allow-groups-list
- Fix authentication method (system-auth) selection and some number of typos

* Wed Sep 09 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.1.2-alt1
- Add sshd-permit-root-login control
- Fix in basealtcontrol ADML
- Fix tcb_chkpwd_restricted to root
- Fix duplicate naming (Accounts service)
- NTP Applier switch added

* Wed Jul 01 2020 Evgeny Sinelnikov <sin@altlinux.org> 0.1.1-alt1
- Update admx according to gpupdate-0.7.0 release

* Mon May 18 2020 Rustem Bapin <rbapin@altlinux.org> 0.1.0-alt1
- Initial release
