* ===============================
* Two Stage Opamp (Parametrized)
* ===============================

.param W_bias_p=610n
.param W_bias_n=4u
.param Lch=180n

.subckt TWO_STAGE_OPAMP In_Inv In_NonInv Vout Vdd Vss \
+ W1 W2 W3 W4 W5 W6 W7 Cc Rz

    * Bias Network
    M_bias_p1 Bias Bias Vdd Vdd P1 w={W_bias_p} l={Lch}
    M_bias_n1 Bias Bias Vss Vss N1 w={W_bias_n} l={Lch}

    * Tail current
    M5 Tail Bias Vss Vss N1 w={W5} l={Lch}

    * Differential pair
    M1 Node_M1 In_Inv Tail Vss N1 w={W1} l={Lch}
    M2 Node_M2 In_NonInv Tail Vss N1 w={W2} l={Lch}
    
    * Current mirror load
    M3 Node_M1 Node_M1 Vdd Vdd P1 w={W3} l={Lch}
    M4 Node_M2 Node_M1 Vdd Vdd P1 w={W4} l={Lch}

    * Second stage
    M6 Vout Node_M2 Vdd Vdd P1 w={W6} l={Lch}
    M7 Vout Bias Vss Vss N1 w={W7} l={Lch}

    * Compensation
    Rz Node_M2 Node_Comp {Rz}
    Cc Node_Comp Vout {Cc}

.ends TWO_STAGE_OPAMP
