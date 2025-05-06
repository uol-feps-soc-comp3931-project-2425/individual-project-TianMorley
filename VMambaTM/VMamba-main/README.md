# VMambaTM

This folder and its subdirectories contain the VMambTM model implementation, as described in the accompanying report.  
The original `README.md` from the VMamba authors is included for licensing purposes and as a reference for setup, usage, and architecture details.

## Custom Modifications

The following modifications were made to support experimental extensions:

- **Low-Rank Factorisation of the SSM Kernel**  
  Implemented in `vmamba.py` at **line 300**.  
  Approximates the state propagation matrix \( A \) as \( A \approx UV^\top \), reducing parameter complexity from \( O(N^2) \) to \( O(2Nr) \).

- **Early Stopping**  
  Implemented in `main.py` at **line 142**.  
  Monitors validation performance and terminates training if no improvement is seen after a specified patience threshold.

- **Fourier Positional Encoding**  
  Defined in `main.py` at **line 47**, applied at **line 318**.  
  Adds fixed sinusoidal encoding to the input image tensor to embed spatial information into early representations.

---

### Notes

- All modifications are toggleable via the configuration file (`config.py`), under the `MODEL.VSSM` namespace.
- The project uses the PyTorch framework and is compatible with multi-GPU training via `torchrun`.
