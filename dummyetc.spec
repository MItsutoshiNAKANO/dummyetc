#
# spec file for package dummyetc
#
# Copyright (c) 2014 Mitsutoshi NAKANO <bkbin005@rinku.zaq.ne.jp>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

Name:           dummyetc
Version:        0
Release:        0
Summary:        Create dummy config file /etc/dummyetc.conf
License:        GPL-3.0+ and PDDL-1.0
Group:          System/Management
Url:            https://github.com/MItsutoshiNAKANO/dummyetc/
Source0:        https://dl.dropboxusercontent.com/u/86335040/dummyetc/%{name}_%{version}.orig.tar.gz
#BuildRequires:  
#Requires:       
BuildArch:      noarch

%description
create dummy config file. (/etc/dummyetc.conf).
for debugging etckeeper.

%prep
%setup -q

%build
%configure

%install
make install DESTDIR=%{buildroot}

%files
%defattr(-, root, root)
%doc COPYING
%config %{_sysconfdir}/dummyetc.conf

%changelog
