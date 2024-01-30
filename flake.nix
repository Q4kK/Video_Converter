{
  description = "My rust flake";


  outputs = { self, nixpkgs }:
    let pkgs = import nixpkgs{system = "x86_64-linux";};

    in {

    devShell.x86_64-linux = pkgs.mkShell {

      packages = [
        pkgs.poetry
        pkgs.python3
        pkgs.python311Packages.ffmpeg-python
        pkgs.python311Packages.python-lsp-server
      ];
    };

 };
}