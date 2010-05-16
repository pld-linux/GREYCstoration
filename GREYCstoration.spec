#
Summary:	Open source algorithms for image denoising and interpolation
Name:		GREYCstoration
Version:	2.9
Release:	1
License:	distributable
Group:		Applications
Source0:	http://dl.sourceforge.net/cimg/%{name}-%{version}-src.zip
# Source0-md5:	c650002008f91ee6409ac78452bc20a1
URL:		http://cimg.sourceforge.net/greycstoration/
BuildRequires:	gimp-devel >= 1:2.0.0
BuildRequires:	unzip
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	libpng-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%(gimptool --gimpplugindir)/plug-ins
%define		_scriptdir	%(gimptool --gimpdatadir)/scripts

%description
GREYCstoration is an image regularization algorithm which is able to process a
color image by locally removing small variations of pixel intensities while
preserving significant global image features, such as edges and corners. The
most direct application of image regularization is image denoising. By
extension, it can also be used to inpaint or resize images.

GREYCstoration is based on state-of-the-art image processing methods using
nonlinear multi-valued diffusion PDE's (Partial Differential Equations). This
kind of method generally outperforms basic image filtering techniques (such as
convolution, median filtering, etc.), classically encountered in image painting
programs.

%package -n gimp-plugin-%{name}
Summary:	GIMP plugin for image denoising and interpolation
Group:		X11/Applications/Graphics
Obsoletes:	gimp-plugin-greycstoration

%description -n gimp-plugin-%{name}

%prep
%setup -q -n %{name}-%{version}-src
ln -s src/CImg.h src/plugins .

%build
%{__make} linux -C src \
	GREYCSTORATION_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_plugindir}}

install src/greycstoration $RPM_BUILD_ROOT%{_bindir}
install src/greycstoration4gimp $RPM_BUILD_ROOT%{_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Licence_CeCILL_V2-en.txt README.txt
%attr(755,root,root) %{_bindir}/*

%files -n gimp-plugin-%{name}
%defattr(644,root,root,755)
%doc Licence_CeCILL_V2-en.txt README.txt
%attr(755,root,root) %{_plugindir}/*
