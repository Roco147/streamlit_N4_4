import streamlit as st
from mi_negocio_N4_4 import *
from calculos_N4_4 import *
from pdf_presupuesto_N4_4 import *

st.title(NOMBRE_NEGOCIO)
st.caption(f"Rubro: {RUBRO}")

if "ingresado" not in st.session_state:
    st.session_state["ingresado"] = False

nombre = st.text_input("Nombre del cliente")

if st.button("Iniciar pedido"):
    if nombre:
        st.session_state["ingresado"] = True

if st.session_state["ingresado"]:
    st.subheader("Selección de productos")
    
    col1, col2 = st.columns(2)
    with col1:
        prod1 = st.selectbox("Producto 1", productos, index=0)
        prod2 = st.selectbox("Producto 2", productos, index=1)
        prod3 = st.selectbox("Producto 3", productos, index=2)
    with col2:
        cant1 = st.number_input("Cantidad 1", value=1, min_value=0)
        cant2 = st.number_input("Cantidad 2", value=0, min_value=0)
        cant3 = st.number_input("Cantidad 3", value=0, min_value=0)

    pago = st.radio("Forma de pago", [EFECTIVO, TRANSFERENCIA])

    pos1 = buscar_posicion(productos, prod1)
    pos2 = buscar_posicion(productos, prod2)
    pos3 = buscar_posicion(productos, prod3)

    prec1 = precios[pos1]
    prec2 = precios[pos2]
    prec3 = precios[pos3]

    subtotal = (cant1 * prec1) + (cant2 * prec2) + (cant3 * prec3)
    con_desc = aplicar_descuento(subtotal, pago)
    descuento = subtotal - con_desc
    iva = calcular_iva(con_desc)
    total = con_desc + iva

    st.write("---")
    st.write(f"**Resumen de pedido para {nombre}**")
    st.write(f"Subtotal: ${subtotal:.2f}")
    st.write(f"Descuento: -${descuento:.2f}")
    st.write(f"IVA: +${iva:.2f}")
    st.metric("TOTAL FINAL", f"${total:.2f}")

    fecha_hoy = "2026-10-07"

    archivo_pdf = armar_pdf(
        numero=1,
        fecha=fecha_hoy,
        cliente=nombre,
        prod1=prod1, cant1=cant1, prec1=prec1,
        prod2=prod2, cant2=cant2, prec2=prec2,
        prod3=prod3, cant3=cant3, prec3=prec3,
        subtotal=subtotal,
        descuento=descuento,
        iva=iva,
        total=total
    )

    st.download_button(
        label="Descargar presupuesto (PDF)",
        data=archivo_pdf,
        file_name=f"presupuesto_{nombre}.pdf",
        mime="application/pdf"
    )