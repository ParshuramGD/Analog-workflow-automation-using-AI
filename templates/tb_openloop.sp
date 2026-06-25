* --- Simple Open-Loop Testbench (AI Training Ready) ---

* ===============================
* Parameters injected by Python
* ===============================

.param W1={W1}
.param W2={W2}
.param W3={W3}
.param W4={W4}
.param W5={W5}
.param W6={W6}
.param W7={W7}

.param Cc={Cc}
.param Rz={Rz}

.param Lch={Lch}

* ===============================

.include 180nm_bsim3.txt
.include opamp.sp

Vdd Vdd 0 1.8
Vss Vss 0 0

V_In_Inv In_Inv 0 dc 0.9
V_In_NonInv In_NonInv 0 dc 0.9 ac 1

X1 In_Inv In_NonInv Vout Vdd Vss TWO_STAGE_OPAMP

Cout Vout 0 2p

.control

    op

    ac dec 20 1 1G

    set units = degrees

    meas ac dc_gain find vdb(Vout) at=1

    meas ac ugf when vdb(Vout)=-3

    let total_phase = 180 + phase(Vout)

    meas ac phase_margin_val find total_phase at=ugf

    print dc_gain
    print ugf
    print phase_margin_val

.endc

.end
