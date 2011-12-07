%define gimpsubver 2.0

Summary: Help files for GIMP
Name: gimp-help
Version: 2.4.2
Release: 5.1%{?dist}
License: GFDL
Group: Documentation
URL: http://wiki.gimp.org/gimp/GimpDocs
Source: ftp://ftp.gimp.org/pub/gimp/help/gimp-help-%{version}.tar.bz2
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-%(%__id_u -n)-root
BuildRequires: docbook-style-xsl
BuildRequires: gnome-doc-utils
BuildRequires: libxml2
BuildRequires: libxslt
BuildRequires: pkgconfig >= 0.9.0
BuildRequires: gimp-devel >= 2:2.4
BuildRequires: gettext
Requires: gimp >= 2:2.4

%description
This package contains a user manual written for the GNU Image Manipulation
Program.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %buildroot
make DESTDIR=%{buildroot} install

rm -f files.list
cat << EOF > files.list
%%defattr (-, root, root, -)
%%dir %%{_datadir}/gimp/%%{gimpsubver}/help
%%{_datadir}/gimp/%%{gimpsubver}/help/images
EOF
f="$PWD/files.list"

pushd %{buildroot}%{_datadir}/gimp/%{gimpsubver}/help
for dir in *; do
    case "$dir" in
    images)
        ;;
    *)
        echo "%%lang($dir) %%{_datadir}/gimp/%%{gimpsubver}/help/$dir" >> "$f"
        ;;
    esac
done
popd

%clean
rm -rf %buildroot

%files -f files.list
%defattr (-, root, root, -)
%doc AUTHORS ChangeLog COPYING NEWS README TERMINOLOGY

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 2.4.2-5.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Dec 12 2008 Nils Philippsen <nils@redhat.com> - 2.4.2-3
- Merge Review (#225798):
  - quote percent signs written into files list
  - enable parallel make

* Thu Dec 11 2008 Nils Philippsen <nils@redhat.com> - 2.4.2-2
- Merge Review (#225798):
  - ship AUTHORS, ChangeLog, COPYING, NEWS, README, TERMINOLOGY
  - don't own directories included in the gimp package
  - use %%defattr(-, root, root, -)

* Wed Nov 26 2008 Nils Philippsen <nils@redhat.com>
- Group: Documentation

* Fri Oct 10 2008 Nils Philippsen <nphilipp@redhat.com> - 2.4.2-1
- version 2.4.2

* Fri Apr 18 2008 Nils Philippsen <nphilipp@redhat.com> - 2.4.1-1
- version 2.4.1

* Mon Feb 04 2008 Nils Philippsen <nphilipp@redhat.com> - 2.4.0-1
- version 2.4.0
- mark language specific files with %%lang()
- add BR: gettext

* Wed Aug 08 2007 Nils Philippsen <nphilipp@redhat.com> - 2-0.2.0.13
- change licensing tag to GFDL

* Wed Aug 08 2007 Nils Philippsen <nphilipp@redhat.com> - 2-0.1.0.13
- version 2-0.13
- don't use "%%makeinstall ..." but "make DESTDIR=... install" for installing

* Thu Apr 12 2007 Nils Philippsen <nphilipp@redhat.com> - 2-0.1.0.12
- version 2-0.12

* Thu Jan 04 2007 Nils Philippsen <nphilipp@redhat.com> - 2-0.1.0.11
- version 2-0.11
- add disttag

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2-0.1.0.10.1.1
- rebuild

* Mon Apr 24 2006 Nils Philippsen <nphilipp@redhat.com>
- version 2-0.10

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Oct 21 2005 Nils Philippsen <nphilipp@redhat.com>
- version 2-0.9

* Wed Feb 23 2005 Nils Philippsen <nphilipp@redhat.com>
- version 2-0.7

* Sat Jan 15 2005 Nils Philippsen <nphilipp@redhat.com>
- version 2-0.6

* Fri Jul 02 2004 Nils Philippsen <nphilipp@redhat.com>
- version 2-0.3

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Apr 02 2004 Nils Philippsen <nphilipp@redhat.com>
- version 2-0.2

* Wed Mar 17 2004 Nils Philippsen <nphilipp@redhat.com>
- version 2-0.1
- initial build
