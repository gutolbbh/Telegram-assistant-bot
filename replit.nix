
{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.pillow
    pkgs.python311Packages.pytesseract
    pkgs.python311Packages.setuptools
  ];
}
