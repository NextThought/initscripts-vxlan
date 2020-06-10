Name:		initscripts-vxlan
Version:	0.2
Release:	1%{?dist}
Summary:	vxlan ifup/down scripts
Packager:       Eugene Paniot <e.paniot@gmail.com>
Group:		System Environment/Base
License:	GPLv2 and GPLv2+
URL:		https://github.com/NextThought/initscripts-vxlan

Source:		%{name}-%{version}.tar.gz

Requires:	initscripts >= 9.49.30
Requires:	iproute >= 3.10

BuildArch:	noarch

%description
initscripts-macvlan provides scripts to manage macvlan netwok intefaces on the host machine

%prep
%setup -q


%install
%{__mkdir} -p %{buildroot}/etc/sysconfig/network-scripts

%{__install} -p -m 0755 ifup-vxlan   %{buildroot}/etc/sysconfig/network-scripts/
%{__install} -p -m 0755 ifdown-vxlan %{buildroot}/etc/sysconfig/network-scripts/

%files
%defattr(-,root,root)
/etc/sysconfig/network-scripts/ifup-vxlan
/etc/sysconfig/network-scripts/ifdown-vxlan

%doc


%changelog
* Wed Jun 10 2020 Sean Jones <sean.jones@nextthought.com> - 0.2
- Update to support static flooding and VXLANs not bound to a single interface
- Set package arch to noarch

* Thu Aug 16 2018 Eugene Paniot <e.paniot@gmail.com> - 0.1
- Initial RPM release
