Capfit-port-scanner

A fast, banner-grabbing TCP port scanner built in Python — built in Kumasi, GH.

## The Story Behind It
I was scanning 8.8.8.8 on my phone hotspot and got 12+ ports showing OPEN. I thought I found something huge. 

It was fake. My ISP's hotspot NAT fakes open ports.

So I rebuilt the scanner to PROVE real vs fake.

Solution:
1. Scan 127.0.0.1 first (your own machine) - ground truth
2. Run `python -m http.server 80` to create a KNOWN open port
3. Fast scan with threading + banner grab - fakes never give banners

## What It Found (Real Results)
[+] Port    80 OPEN -> HTTP/1.0 200 OK   # My own http.server - PROOF it's real

[+] Port   135 OPEN -> (open, no banner) # Windows RPC

[+] Port   445 OPEN -> (open, no banner) # Windows SMB
