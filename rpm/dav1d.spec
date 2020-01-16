Name:           dav1d
Version:        1.5.1
Release:        1
Summary:        AV1 cross-platform Decoder
License:        BSD
URL:            https://code.videolan.org/videolan/dav1d
Source0:        %{name}-%{version}.tar.bz2

%ifarch i486 x86_64
BuildRequires:  nasm
%endif
BuildRequires:  doxygen
BuildRequires:  meson >= 0.47.0

%description
dav1d is a new AV1 cross-platform Decoder, open-source, and focused on speed
and correctness.

%package -n libdav1d
Summary:        Library files for dav1d

%description -n libdav1d
Library files for dav1d, the AV1 cross-platform Decoder.

%package -n libdav1d-devel
Summary:        Development files for dav1d
Requires:       libdav1d%{?_isa} = %{version}-%{release}

%description -n libdav1d-devel
Development files for dav1d, the AV1 cross-platform Decoder.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
%meson --buildtype=release \
       -Denable_tests=false \
       -Dxxhash_muxer=disabled

%meson_build

%install
%meson_install

%post -n libdav1d -p /sbin/ldconfig
%postun -n libdav1d -p /sbin/ldconfig

%files
%license COPYING doc/PATENTS
%doc CONTRIBUTING.md NEWS README.md
%{_bindir}/dav1d

%files -n libdav1d
%license COPYING doc/PATENTS
%{_libdir}/libdav1d.so.*

%files -n libdav1d-devel
%{_includedir}/%{name}
%{_libdir}/libdav1d.so
%{_libdir}/pkgconfig/%{name}.pc
