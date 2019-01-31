%define distroversion 7.6.1810
%define distrorelease final

Summary: NethServer YUM repo configuration
Name: nethserver-release
Version: 7
Release: 12%{?dist}
License: GPL
BuildArch: noarch
Source: %{name}-%{version}.tar.gz
URL: %{url_prefix}/%{name}

BuildRequires: nethserver-devtools

%description
NethServer YUM repository configuration

%prep
%setup

%build
perl createlinks
echo %{distroversion} > root/etc/e-smith/db/configuration/force/sysconfig/Version
echo %{distrorelease} > root/etc/e-smith/db/configuration/force/sysconfig/Release
echo "NethServer release %{distroversion} (%{distrorelease})" > root/etc/%{name}
%{__install} -d root/%{_nseventsdir}/%{name}-update

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -not -name '*.orig' -print  | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%doc COPYING
%config(noreplace) /etc/yum.repos.d/NethServer.repo
%dir %{_nseventsdir}/%{name}-update

%changelog
* Fri Dec 17 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 7-12
- Improve installation on CentOS

* Thu Dec 13 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 7-11
- NethServer 7.6.1810 final

* Fri Dec 07 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 7-10
- NethServer 7.6.1810 beta2

* Mon Dec 03 2018 Davide Principi <davide.principi@nethesis.it> - 7-9
- NethServer 7.6.1810 beta

* Fri Jun 08 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 7-8
- NethServer 7.5.1804 final
- Fix nethserver-config-network not enabled - NethServer/dev#5520

* Wed May 30 2018 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 7-7
- NethServer 7.5.1804 rc

* Wed May 16 2018 Davide Principi <davide.principi@nethesis.it> - 7-6
- NethServer 7.5.1804 beta (rebased on CentOS 7.5.1804)

* Fri Oct 27 2017 Davide Principi <davide.principi@nethesis.it> - 7-5
- Fix version lock

* Mon Oct 23 2017 Davide Principi <davide.principi@nethesis.it> - 7-4
- Rebase on CentOS 7.4.1708

* Wed Mar 01 2017 Davide Principi <davide.principi@nethesis.it> - 7-3
- nethserver-install: Unit NetworkManager.service not loaded - Bug NethServer/dev#5226

* Tue Feb 14 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 7-2
- Install on CentOS: nethserver-install fails - NethServer/dev#5218

* Mon Jan 30 2017 Davide Principi <davide.principi@nethesis.it> - 7-1
- NethServer 7 final release

* Tue Jan 17 2017 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 7-0.7
- NethServer 7 rc4 release

* Thu Dec 15 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 7-0.6
- NethServer 7 rc3 release

* Wed Nov 09 2016 Davide Principi <davide.principi@nethesis.it> - 7-0.5
- NethServer 7 rc2 release

* Tue Oct 18 2016 Davide Principi <davide.principi@nethesis.it> - 7-0.4
- NethServer 7 rc1 release

* Thu Jul 07 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 7-0.3
- NethServer 7 beta2 release

* Thu Jul 07 2016 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 7-0.2
- NethServer 7 beta1 release
