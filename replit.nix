{ pkgs }: {
  deps = [
    pkgs.python39
    pkgs.python39Packages.fastapi
    pkgs.python39Packages.uvicorn
    pkgs.python39Packages.httpx
    pkgs.python39Packages.python-dotenv
  ];
}
