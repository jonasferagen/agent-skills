# Project foundation extraction

The framework moves to https://github.com/jonasferagen/project-foundation.
Clear-writing, diagrams-and-tables and source-of-truth remain standalone source
packages here. Their new versions remove hard-coded framework dependencies;
the framework imports their complete directories at an explicit source commit.

The selected source baseline is `9093cfca4ffa93df1be35b1bb7ebffaef0baac65`, including
the landed 1.5.0 process format and its declaration hardening. Framework-specific
validation and native source history follow the new repository. Generic validation
stays here. Links to removed historical artifacts identify that original revision.

## Verification

Migration verification and routing trials are pending. A source-package move
does not itself establish standalone selection, framework routing or consumer adoption.
