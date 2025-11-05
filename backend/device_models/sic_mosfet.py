class SiCMOSFET:
    def __init__(self, v_gs, v_ds, r_on, c_gs, c_ds):
        self.v_gs = v_gs  # Gate-source voltage
        self.v_ds = v_ds  # Drain-source voltage
        self.r_on = r_on  # On-resistance
        self.c_gs = c_gs  # Gate-source capacitance
        self.c_ds = c_ds  # Drain-source capacitance

    def calculate_current(self):
        """Calculate the drain current based on Vgs and Vds."""
        if self.v_gs > 0:
            return (self.v_gs - self.v_ds) / self.r_on
        return 0

    def calculate_power_loss(self):
        """Calculate the power loss in the MOSFET."""
        current = self.calculate_current()
        return current ** 2 * self.r_on

    def get_capacitance(self):
        """Return the gate-source and drain-source capacitance."""
        return self.c_gs, self.c_ds

    def __str__(self):
        return f"SiC MOSFET: Vgs={self.v_gs}, Vds={self.v_ds}, Ron={self.r_on}, Cgs={self.c_gs}, Cds={self.c_ds}"