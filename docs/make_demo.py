#!/usr/bin/env -S uv run --script --quiet
# /// script
# requires-python = ">=3.10"
# dependencies = ["qrcode>=7", "rich>=13"]
# ///
"""Regenerate the README demo image.

This writes demo.svg; rasterize it with a real browser so the embedded
webfont renders the QR's half-block glyphs correctly (cairosvg mangles them):

    chrome --headless=new --screenshot=demo.png --window-size=2038,1272 \
           --hide-scrollbars --virtual-time-budget=10000 file://.../demo.svg
"""

import io
import pathlib

import qrcode
from rich.console import Console

qr = qrcode.QRCode(border=2)
qr.add_data("WIFI:T:ADB;S:adbqr-3f9a17c2;P:kP4mW9xQz2Lr;;")
buf = io.StringIO()
qr.print_ascii(out=buf, invert=True)

console = Console(record=True, width=82)
console.print("[bold green]$[/] [bold]adb-qr[/]")
console.print(buf.getvalue().rstrip("\n"), markup=False, highlight=False)
console.print("On the phone: Developer options > Wireless debugging > Pair device with QR code")
console.print("Waiting for scan (up to 120s)... [cyan]found 192.168.1.42:40331[/]")
console.print("[green]Successfully paired to 192.168.1.42:40331 \\[guid=adb-1A2B3C4D-aBcDeF][/]")
console.print("[bold green]Connected: 192.168.1.42:44915[/]")
console.save_svg(str(pathlib.Path(__file__).parent / "demo.svg"), title="adb-qr")
