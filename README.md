# x32-iexplore-calc-injector-Dynamic-WinExec-Shellcode-PoC
A 32-bit PE Code-Cave &amp; Dynamic PEB Shellcode PoC demonstrating arbitrary payload execution (calc.exe) upon launching Internet Explorer (iexplore.exe).


Core Workflow Checklist:

Section Inspection: Locate custom .OwO RVA via x32dbg Memory Map.

Payload Injection: Generate 4-byte aligned Opcode stream via LocalShellcode.py.

Binary Patching: Clear stale bytes using Fill with NOPs (Ctrl+9), then apply Paste (Ignore Size).

Stack Restoration: Adjust ADD ESP, <offset> to match the total byte count of the pushed string, preserving register state before POPAD.


Binary Export: Persist changes directly into PE executable via File -> Patch File.

I lean finding kernel32 base from Red Team Note. Thank of them 

https://www.ired.team/offensive-security/code-injection-process-injection/finding-kernel32-base-and-function-addresses-in-shellcode
