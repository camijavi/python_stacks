"""
Simulador interactivo de Pila (Stack) en terminal estilo Python Tutor.
Replica con fidelidad el diagrama visual de memoria (Frames & Objects) y los
botones de navegación interactiva (<< First, < Prev, Next >, Last >>).
"""

import sys
import os

# Códigos ANSI para colores
BLUE = "\033[94m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GRAY = "\033[90m"
BOLD = "\033[1m"
RESET = "\033[0m"


def clear_screen():
    if sys.stdout.isatty():
        sys.stdout.write("\033[2J\033[H")
        sys.stdout.flush()
    else:
        print("\n" * 2)


SOURCE_CODE = [
    (1, "from stack import Stack, Producto"),
    (2, ""),
    (3, "def main():"),
    (4, "    pila = Stack()"),
    (5, '    prod = Producto("P-01", "Mascarilla", 15.23, 6200)'),
    (6, "    pila.push(prod)"),
    (7, '    prod = Producto("P-02", "Alcohol", 64.54, 1000)'),
    (8, "    pila.push(prod)"),
    (9, '    prod = Producto("P-03", "vitamina", 21.85, 7000)'),
    (10, "    pila.push(prod)"),
    (11, "    productos = pila.clear()"),
    (12, "    for p in productos:"),
    (13, "        p.print()"),
    (14, ""),
    (15, "main()")
]


def render_full_diagram_image1() -> str:
    """
    Renderiza el diagrama de memoria réplica exacta de la imagen de Python Tutor:
    - Frames (Global frame: Producto, Stack, pila, prod)
    - Objects:
        - Producto class
        - Stack class
        - Stack instance (top apunta a P-03 al fondo)
        - Producto instance (P-01) en la parte superior derecha
        - Producto instance (P-02) en medio con next apuntando hacia arriba a P-01
        - Producto instance (P-03) al fondo con next apuntando hacia arriba a P-02
    """
    lines = [
        f"{BOLD}{BLUE}Frames{RESET}                  {BOLD}{YELLOW}Objects{RESET}",
        "",
        f"{BOLD}{BLUE}Global frame{RESET}            {BOLD}{YELLOW}Producto class{RESET}",
        f"{GRAY}┌──────────┬───┐{RESET}        {GRAY}┌──────────┬───────────────────────────────────────────┐{RESET}",
        f"{GRAY}│{RESET} Producto {GRAY}│{RESET} {CYAN}●{RESET} {GRAY}│{RESET}{CYAN}───────►{RESET}{GRAY}│{RESET} __init__ {GRAY}│{RESET} function                                  {GRAY}│{RESET}",
        f"{GRAY}├──────────┼───┤{RESET}        {GRAY}│{RESET}          {GRAY}│{RESET} __init__(self, cod, nombre, precio, stock){GRAY}│{RESET}",
        f"{GRAY}│{RESET} Stack    {GRAY}│{RESET} {CYAN}●{RESET} {GRAY}│{RESET}{CYAN}───┐{RESET}    {GRAY}└──────────┴───────────────────────────────────────────┘{RESET}",
        f"{GRAY}├──────────┼───┤{RESET}   {CYAN}│{RESET}",
        f"{GRAY}│{RESET} pila     {GRAY}│{RESET} {CYAN}●{RESET} {GRAY}│{RESET}{CYAN}─┐{RESET} {CYAN}│{RESET}    {BOLD}{YELLOW}Stack class{RESET}",
        f"{GRAY}├──────────┼───┤{RESET} {CYAN}│{RESET} {CYAN}│{RESET}    {GRAY}┌──────────┬────────────────────────┐{RESET}",
        f"{GRAY}│{RESET} prod     {GRAY}│{RESET} {CYAN}●{RESET} {GRAY}│{RESET}{CYAN}┐│{RESET} {CYAN}└───►{RESET}{GRAY}│{RESET} __init__ {GRAY}│{RESET} function               {GRAY}│{RESET}",
        f"{GRAY}└──────────┴───┘{RESET}{CYAN}││{RESET}      {GRAY}│{RESET}          {GRAY}│{RESET} __init__(self)         {GRAY}│{RESET}",
        f"                {CYAN}││{RESET}      {GRAY}├──────────┼────────────────────────┤{RESET}",
        f"                {CYAN}││{RESET}      {GRAY}│{RESET} isEmpty  {GRAY}│{RESET} function               {GRAY}│{RESET}",
        f"                {CYAN}││{RESET}      {GRAY}│{RESET}          {GRAY}│{RESET} isEmpty(self)          {GRAY}│{RESET}",
        f"                {CYAN}││{RESET}      {GRAY}├──────────┼────────────────────────┤{RESET}",
        f"                {CYAN}││{RESET}      {GRAY}│{RESET} push     {GRAY}│{RESET} function               {GRAY}│{RESET}",
        f"                {CYAN}││{RESET}      {GRAY}│{RESET}          {GRAY}│{RESET} push(self, new)        {GRAY}│{RESET}",
        f"                {CYAN}││{RESET}      {GRAY}└──────────┴────────────────────────┘{RESET}",
        f"                {CYAN}││{RESET}",
        f"                {CYAN}││{RESET}      {BOLD}{YELLOW}Stack instance{RESET}",
        f"                {CYAN}││{RESET}      {GRAY}┌──────┬───┐{RESET}",
        f"                {CYAN}│└─────►{RESET}{GRAY}│{RESET} top  {GRAY}│{RESET} {CYAN}●{RESET} {GRAY}│{RESET}{CYAN}──────────────────────────────┐{RESET}",
        f"                {CYAN}│{RESET}       {GRAY}└──────┴───┘{RESET}                              {CYAN}│{RESET}",
        f"                {CYAN}│{RESET}                                                 {CYAN}│{RESET}",
        f"                {CYAN}│{RESET}                                                 {CYAN}▼{RESET}",
        f"                {CYAN}│{RESET}                                        {BOLD}{YELLOW}Producto instance{RESET}",
        f"                {CYAN}│{RESET}                                        {GRAY}┌────────┬──────────────┐{RESET}",
        f"                {CYAN}│{RESET}                                        {GRAY}│{RESET} cod    {GRAY}│{RESET} {WHITE}\"P-01\"{RESET}       {GRAY}│{RESET}",
        f"                {CYAN}│{RESET}                                        {GRAY}├────────┼──────────────┤{RESET}",
        f"                {CYAN}│{RESET}                                        {GRAY}│{RESET} next   {GRAY}│{RESET} {CYAN}None{RESET}         {GRAY}│{RESET}",
        f"                {CYAN}│{RESET}                                        {GRAY}├────────┼──────────────┤{RESET}",
        f"                {CYAN}│{RESET}                                        {GRAY}│{RESET} nombre {GRAY}│{RESET} {WHITE}\"Mascarilla\"{RESET} {GRAY}│{RESET}",
        f"                {CYAN}│{RESET}                                        {GRAY}├────────┼──────────────┤{RESET}",
        f"                {CYAN}│{RESET}                                        {GRAY}│{RESET} precio {GRAY}│{RESET} {WHITE}15.23{RESET}        {GRAY}│{RESET}",
        f"                {CYAN}│{RESET}                                        {GRAY}├────────┼──────────────┤{RESET}",
        f"                {CYAN}│{RESET}                                        {GRAY}│{RESET} stock  {GRAY}│{RESET} {WHITE}6200{RESET}         {GRAY}│{RESET}",
        f"                {CYAN}│{RESET}                                        {GRAY}└────────┴──────────────┘{RESET}",
        f"                {CYAN}│{RESET}                                                   {CYAN}▲{RESET}",
        f"                {CYAN}│{RESET}                                                   {CYAN}│{RESET}",
        f"                {CYAN}│{RESET}                                {BOLD}{YELLOW}Producto instance{RESET}  {CYAN}│{RESET}",
        f"                {CYAN}│{RESET}                                {GRAY}┌────────┬─────────┴────┐{RESET}",
        f"                {CYAN}│{RESET}                                {GRAY}│{RESET} cod    {GRAY}│{RESET} {WHITE}\"P-02\"{RESET}       {GRAY}│{RESET}",
        f"                {CYAN}│{RESET}                                {GRAY}├────────┼──────────────┤{RESET}",
        f"                {CYAN}│{RESET}                                {GRAY}│{RESET} next   {GRAY}│{RESET}    {CYAN}●─────────┘{RESET}",
        f"                {CYAN}│{RESET}                                {GRAY}├────────┼──────────────┤{RESET}",
        f"                {CYAN}│{RESET}                                {GRAY}│{RESET} nombre {GRAY}│{RESET} {WHITE}\"Alcohol\"{RESET}    {GRAY}│{RESET}",
        f"                {CYAN}│{RESET}                                {GRAY}├────────┼──────────────┤{RESET}",
        f"                {CYAN}│{RESET}                                {GRAY}│{RESET} precio {GRAY}│{RESET} {WHITE}64.54{RESET}        {GRAY}│{RESET}",
        f"                {CYAN}│{RESET}                                {GRAY}├────────┼──────────────┤{RESET}",
        f"                {CYAN}│{RESET}                                {GRAY}│{RESET} stock  {GRAY}│{RESET} {WHITE}1000{RESET}         {GRAY}│{RESET}",
        f"                {CYAN}│{RESET}                                {GRAY}└────────┴──────────────┘{RESET}",
        f"                {CYAN}│{RESET}                                          {CYAN}▲{RESET}",
        f"                {CYAN}│{RESET}                                          {CYAN}│{RESET}",
        f"                {CYAN}│{RESET}       {BOLD}{YELLOW}Producto instance{RESET}                  {CYAN}│{RESET}",
        f"                {CYAN}│{RESET}       {GRAY}┌────────┬─────────────────────────┴┐{RESET}",
        f"                {CYAN}└──────►{RESET}{GRAY}│{RESET} cod    {GRAY}│{RESET} {WHITE}\"P-03\"{RESET}                   {GRAY}│{RESET}",
        f"                        {GRAY}├────────┼──────────────────────────┤{RESET}",
        f"                        {GRAY}│{RESET} next   {GRAY}│{RESET}    {CYAN}●─────────────────────┘{RESET}",
        f"                        {GRAY}├────────┼──────────────────────────┤{RESET}",
        f"                        {GRAY}│{RESET} nombre {GRAY}│{RESET} {WHITE}\"vitamina\"{RESET}               {GRAY}│{RESET}",
        f"                        {GRAY}├────────┼──────────────────────────┤{RESET}",
        f"                        {GRAY}│{RESET} precio {GRAY}│{RESET} {WHITE}21.85{RESET}                    {GRAY}│{RESET}",
        f"                        {GRAY}├────────┼──────────────────────────┤{RESET}",
        f"                        {GRAY}│{RESET} stock  {GRAY}│{RESET} {WHITE}7000{RESET}                     {GRAY}│{RESET}",
        f"                        {GRAY}└────────┴──────────────────────────┘{RESET}",
    ]
    return "\n".join(lines)


def render_partial_diagram(num_items: int) -> str:
    """Renderiza estados intermedios antes de completar los 3 productos."""
    if num_items >= 3:
        return render_full_diagram_image1()

    lines = [
        f"{BOLD}{BLUE}Frames{RESET}                  {BOLD}{YELLOW}Objects{RESET}",
        "",
        f"{BOLD}{BLUE}Global frame{RESET}            {BOLD}{YELLOW}Producto class{RESET}",
        f"{GRAY}┌──────────┬───┐{RESET}        {GRAY}┌──────────┬───────────────────────────────────────────┐{RESET}",
        f"{GRAY}│{RESET} Producto {GRAY}│{RESET} {CYAN}●{RESET} {GRAY}│{RESET}{CYAN}───────►{RESET}{GRAY}│{RESET} __init__ {GRAY}│{RESET} function                                  {GRAY}│{RESET}",
        f"{GRAY}├──────────┼───┤{RESET}        {GRAY}│{RESET}          {GRAY}│{RESET} __init__(self, cod, nombre, precio, stock){GRAY}│{RESET}",
        f"{GRAY}│{RESET} Stack    {GRAY}│{RESET} {CYAN}●{RESET} {GRAY}│{RESET}{CYAN}───┐{RESET}    {GRAY}└──────────┴───────────────────────────────────────────┘{RESET}",
        f"{GRAY}├──────────┼───┤{RESET}   {CYAN}│{RESET}",
        f"{GRAY}│{RESET} pila     {GRAY}│{RESET} {CYAN}●{RESET} {GRAY}│{RESET}{CYAN}─┐{RESET} {CYAN}│{RESET}    {BOLD}{YELLOW}Stack class{RESET}",
        f"{GRAY}├──────────┼───┤{RESET} {CYAN}│{RESET} {CYAN}│{RESET}    {GRAY}┌──────────┬────────────────────────┐{RESET}",
        f"{GRAY}│{RESET} prod     {GRAY}│{RESET} {CYAN}●{RESET} {GRAY}│{RESET}{CYAN}┐│{RESET} {CYAN}└───►{RESET}{GRAY}│{RESET} __init__ {GRAY}│{RESET} function               {GRAY}│{RESET}",
        f"{GRAY}└──────────┴───┘{RESET}{CYAN}││{RESET}      {GRAY}│{RESET}          {GRAY}│{RESET} __init__(self)         {GRAY}│{RESET}",
        f"                {CYAN}││{RESET}      {GRAY}├──────────┼────────────────────────┤{RESET}",
        f"                {CYAN}││{RESET}      {GRAY}│{RESET} isEmpty  {GRAY}│{RESET} function               {GRAY}│{RESET}",
        f"                {CYAN}││{RESET}      {GRAY}├──────────┼────────────────────────┤{RESET}",
        f"                {CYAN}││{RESET}      {GRAY}│{RESET} push     {GRAY}│{RESET} function               {GRAY}│{RESET}",
        f"                {CYAN}││{RESET}      {GRAY}└──────────┴────────────────────────┘{RESET}",
        f"                {CYAN}││{RESET}",
        f"                {CYAN}││{RESET}      {BOLD}{YELLOW}Stack instance{RESET}",
        f"                {CYAN}││{RESET}      {GRAY}┌──────┬───────┐{RESET}",
    ]

    if num_items == 0:
        lines.append(f"                {CYAN}│└─────►{RESET}{GRAY}│{RESET} top  {GRAY}│{RESET} {CYAN}None{RESET}  {GRAY}│{RESET} (Pila vacía)")
        lines.append(f"                {CYAN}│{RESET}       {GRAY}└──────┴───────┘{RESET}")
    elif num_items == 1:
        lines.append(f"                {CYAN}│└─────►{RESET}{GRAY}│{RESET} top  {GRAY}│{RESET}   {CYAN}●{RESET}   {GRAY}│{RESET}{CYAN}──────────────────────┐{RESET}")
        lines.append(f"                {CYAN}│{RESET}       {GRAY}└──────┴───────┘{RESET}                      {CYAN}│{RESET}")
        lines.append(f"                {CYAN}│{RESET}                                             {CYAN}▼{RESET}")
        lines.append(f"                {CYAN}│{RESET}                                    {BOLD}{YELLOW}Producto instance{RESET}")
        lines.append(f"                {CYAN}│{RESET}                                    {GRAY}┌────────┬──────────────┐{RESET}")
        lines.append(f"                {CYAN}└──────────────────────────────────►{RESET}{GRAY}│{RESET} cod    {GRAY}│{RESET} {WHITE}\"P-01\"{RESET}       {GRAY}│{RESET}")
        lines.append(f"                                                    {GRAY}├────────┼──────────────┤{RESET}")
        lines.append(f"                                                    {GRAY}│{RESET} next   {GRAY}│{RESET} {CYAN}None{RESET}         {GRAY}│{RESET}")
        lines.append(f"                                                    {GRAY}├────────┼──────────────┤{RESET}")
        lines.append(f"                                                    {GRAY}│{RESET} nombre {GRAY}│{RESET} {WHITE}\"Mascarilla\"{RESET} {GRAY}│{RESET}")
        lines.append(f"                                                    {GRAY}├────────┼──────────────┤{RESET}")
        lines.append(f"                                                    {GRAY}│{RESET} precio {GRAY}│{RESET} {WHITE}15.23{RESET}        {GRAY}│{RESET}")
        lines.append(f"                                                    {GRAY}├────────┼──────────────┤{RESET}")
        lines.append(f"                                                    {GRAY}│{RESET} stock  {GRAY}│{RESET} {WHITE}6200{RESET}         {GRAY}│{RESET}")
        lines.append(f"                                                    {GRAY}└────────┴──────────────┘{RESET}")
    elif num_items == 2:
        lines.append(f"                {CYAN}│└─────►{RESET}{GRAY}│{RESET} top  {GRAY}│{RESET}   {CYAN}●{RESET}   {GRAY}│{RESET}{CYAN}──────────────────────┐{RESET}")
        lines.append(f"                {CYAN}│{RESET}       {GRAY}└──────┴───────┘{RESET}                      {CYAN}│{RESET}")
        lines.append(f"                {CYAN}│{RESET}                                             {CYAN}│{RESET}")
        lines.append(f"                {CYAN}│{RESET}                                    {BOLD}{YELLOW}Producto instance{RESET} {CYAN}│{RESET}")
        lines.append(f"                {CYAN}│{RESET}                                    {GRAY}┌────────┬──────────────┐{RESET}")
        lines.append(f"                {CYAN}│{RESET}                                    {GRAY}│{RESET} cod    {GRAY}│{RESET} {WHITE}\"P-01\"{RESET}       {GRAY}│{RESET}")
        lines.append(f"                {CYAN}│{RESET}                                    {GRAY}├────────┼──────────────┤{RESET}")
        lines.append(f"                {CYAN}│{RESET}                                    {GRAY}│{RESET} next   {GRAY}│{RESET} {CYAN}None{RESET}         {GRAY}│{RESET}")
        lines.append(f"                {CYAN}│{RESET}                                    {GRAY}├────────┼──────────────┤{RESET}")
        lines.append(f"                {CYAN}│{RESET}                                    {GRAY}│{RESET} nombre {GRAY}│{RESET} {WHITE}\"Mascarilla\"{RESET} {GRAY}│{RESET}")
        lines.append(f"                {CYAN}│{RESET}                                    {GRAY}└────────┴──────────────┘{RESET}")
        lines.append(f"                {CYAN}│{RESET}                                               {CYAN}▲{RESET}")
        lines.append(f"                {CYAN}│{RESET}                            {BOLD}{YELLOW}Producto instance{RESET}  {CYAN}│{RESET}")
        lines.append(f"                {CYAN}│{RESET}                            {GRAY}┌────────┬─────────┴────┐{RESET}")
        lines.append(f"                {CYAN}└──────────────────────────►{RESET}{GRAY}│{RESET} cod    {GRAY}│{RESET} {WHITE}\"P-02\"{RESET}       {GRAY}│{RESET}")
        lines.append(f"                                            {GRAY}├────────┼──────────────┤{RESET}")
        lines.append(f"                                            {GRAY}│{RESET} next   {GRAY}│{RESET}    {CYAN}●─────────┘{RESET}")
        lines.append(f"                                            {GRAY}├────────┼──────────────┤{RESET}")
        lines.append(f"                                            {GRAY}│{RESET} nombre {GRAY}│{RESET} {WHITE}\"Alcohol\"{RESET}    {GRAY}│{RESET}")
        lines.append(f"                                            {GRAY}└────────┴──────────────┘{RESET}")

    return "\n".join(lines)


# Pasos del simulador con línea ejecutada y siguiente línea
STEPS = [
    {
        "exec_line": 4,
        "next_line": 5,
        "action": "pila = Stack() -> Se crea una nueva instancia de Stack (top = None)",
        "items": 0,
        "stdout": ""
    },
    {
        "exec_line": 5,
        "next_line": 6,
        "action": 'prod = Producto("P-01", "Mascarilla", 15.23, 6200) -> Se crea el objeto P-01',
        "items": 0,
        "stdout": ""
    },
    {
        "exec_line": 6,
        "next_line": 7,
        "action": "pila.push(prod) -> Se apila P-01; top apunta a P-01",
        "items": 1,
        "stdout": ""
    },
    {
        "exec_line": 7,
        "next_line": 8,
        "action": 'prod = Producto("P-02", "Alcohol", 64.54, 1000) -> Se crea el objeto P-02',
        "items": 1,
        "stdout": ""
    },
    {
        "exec_line": 8,
        "next_line": 9,
        "action": "pila.push(prod) -> Se apila P-02; P-02.next apunta a P-01, top apunta a P-02",
        "items": 2,
        "stdout": ""
    },
    {
        "exec_line": 9,
        "next_line": 10,
        "action": 'prod = Producto("P-03", "vitamina", 21.85, 7000) -> Se crea el objeto P-03',
        "items": 2,
        "stdout": ""
    },
    {
        "exec_line": 10,
        "next_line": 11,
        "action": "pila.push(prod) -> Se apila P-03; P-03.next apunta a P-02, top apunta a P-03 (Pila completa)",
        "items": 3,
        "stdout": ""
    },
    {
        "exec_line": 11,
        "next_line": 12,
        "action": "productos = pila.clear() -> Se desapilan los elementos; la pila queda vacía",
        "items": 0,
        "stdout": ""
    },
    {
        "exec_line": 13,
        "next_line": 12,
        "action": "productos[0].print() -> Imprime primer elemento desapilado: P-03",
        "items": 0,
        "stdout": "PRODUCTO --> id = P-03 | NOMBRE vitamina | PRECIO 21.85 | STOCK 7000\n"
    },
    {
        "exec_line": 13,
        "next_line": 12,
        "action": "productos[1].print() -> Imprime segundo elemento desapilado: P-02",
        "items": 0,
        "stdout": "PRODUCTO --> id = P-03 | NOMBRE vitamina | PRECIO 21.85 | STOCK 7000\nPRODUCTO --> id = P-02 | NOMBRE Alcohol | PRECIO 64.54 | STOCK 1000\n"
    },
    {
        "exec_line": 13,
        "next_line": 15,
        "action": "productos[2].print() -> Imprime tercer elemento desapilado: P-01. Fin.",
        "items": 0,
        "stdout": "PRODUCTO --> id = P-03 | NOMBRE vitamina | PRECIO 21.85 | STOCK 7000\nPRODUCTO --> id = P-02 | NOMBRE Alcohol | PRECIO 64.54 | STOCK 1000\nPRODUCTO --> id = P-01 | NOMBRE Mascarilla | PRECIO 15.23 | STOCK 6200\n"
    }
]


def render_step(step_idx: int):
    """Muestra la vista completa del paso, con código, diagrama de memoria, slider y botones."""
    step = STEPS[step_idx]
    total_steps = len(STEPS)

    clear_screen()

    print(f"{BOLD}{CYAN}╔══════════════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"{BOLD}{CYAN}║                   PYTHON TUTOR SIMULATOR - PILA (STACK)                      ║{RESET}")
    print(f"{BOLD}{CYAN}╚══════════════════════════════════════════════════════════════════════════════╝{RESET}")

    # Leyenda exacta de Python Tutor (Imagen 2)
    print(f"  {GREEN}{BOLD}➡{RESET} {GREEN}line that just executed{RESET}")
    print(f"  {RED}{BOLD}➡{RESET} {RED}next line to execute{RESET}\n")

    # Vista de Código Fuente
    print(f"{BOLD}Código (main.py):{RESET}")
    print(f"{GRAY}──────────────────────────────────────────────────────────────────────────────{RESET}")
    for num, code_line in SOURCE_CODE:
        if num == step["exec_line"]:
            prefix = f"{GREEN}{BOLD} ➡ {num:2d} │{RESET} "
            content = f"{GREEN}{BOLD}{code_line}{RESET}"
        elif num == step["next_line"]:
            prefix = f"{RED}{BOLD} ➡ {num:2d} │{RESET} "
            content = f"{RED}{BOLD}{code_line}{RESET}"
        else:
            prefix = f"   {GRAY}{num:2d} │{RESET} "
            content = f"{WHITE}{code_line}{RESET}"
        print(f"{prefix}{content}")
    print(f"{GRAY}──────────────────────────────────────────────────────────────────────────────{RESET}")

    # Explicación de la acción
    print(f"{BOLD}Acción:{RESET} {CYAN}{step['action']}{RESET}\n")

    # Diagrama de Memoria (Frames & Objects exacto a Imagen 1)
    print(render_partial_diagram(step["items"]))

    # Salida por terminal si existe
    if step["stdout"]:
        print(f"\n{BOLD}Salida estándar:{RESET}")
        for sline in step["stdout"].strip().splitlines():
            print(f"  {GREEN}{sline}{RESET}")

    # Slider idéntico a Imagen 2
    slider_width = 46
    curr_pos = int((step_idx / max(1, total_steps - 1)) * (slider_width - 1))
    slider_bar = "─" * curr_pos + "⚪" + "─" * (slider_width - 1 - curr_pos)
    print(f"\n      {slider_bar}")

    # Botones idénticos a Imagen 2
    print(f"     ┌───────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐")
    print(f"     │  << First │  │  < Prev  │  │  Next >  │  │  Last >> │")
    print(f"     └───────────┘  └──────────┘  └──────────┘  └──────────┘")
    print(f"                        {BOLD}Step {step_idx + 1} of {total_steps}{RESET}")
    print(f"  {GRAY}[Teclas: Enter/n = Next, p = Prev, f = First, l = Last, q = Salir]{RESET}")


def get_key_input() -> str:
    """Lee tecla única o input del usuario."""
    prompt = f"{BOLD}Comando [↵: Next, p: Prev, f: First, l: Last, q: Salir]: {RESET}"
    if sys.stdin.isatty():
        try:
            import termios
            import tty
            fd = sys.stdin.fileno()
            old = termios.tcgetattr(fd)
            try:
                tty.setraw(fd)
                sys.stdout.write(prompt)
                sys.stdout.flush()
                ch = sys.stdin.read(1)
                if ch == "\x1b":
                    c2 = sys.stdin.read(1)
                    if c2 == "[":
                        c3 = sys.stdin.read(1)
                        if c3 == "C": return "next"
                        elif c3 == "D": return "prev"
                        elif c3 == "H": return "first"
                        elif c3 == "F": return "last"
                    return ""
                if ch in ("\r", "\n", " ", "n", "N", "3"):
                    return "next"
                elif ch in ("p", "P", "2"):
                    return "prev"
                elif ch in ("f", "F", "1"):
                    return "first"
                elif ch in ("l", "L", "4"):
                    return "last"
                elif ch in ("q", "Q"):
                    return "quit"
                return ch.lower()
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old)
                print()
        except Exception:
            pass

    try:
        val = input(prompt).strip().lower()
        if val in ("", "n", "next"): return "next"
        elif val in ("p", "prev"): return "prev"
        elif val in ("f", "first"): return "first"
        elif val in ("l", "last"): return "last"
        elif val in ("q", "quit", "exit"): return "quit"
        return val
    except (EOFError, KeyboardInterrupt):
        return "quit"


def run_interactive_simulator(start_step: int = 6):
    """Bucle de ejecución con botones de avance y retroceso."""
    current = start_step
    total = len(STEPS)

    while True:
        render_step(current)
        if not sys.stdin.isatty():
            # Si no es interactivo, salir tras mostrar el estado
            break
        cmd = get_key_input()
        if cmd == "next":
            if current < total - 1:
                current += 1
            else:
                print(f"{YELLOW}Has llegado al final (Last >>). Presiona 'q' para salir.{RESET}")
        elif cmd == "prev":
            if current > 0:
                current -= 1
            else:
                print(f"{YELLOW}Estás en el inicio (<< First).{RESET}")
        elif cmd == "first":
            current = 0
        elif cmd == "last":
            current = total - 1
        elif cmd == "quit":
            print(f"{GREEN}Simulación completada.{RESET}\n")
            break


def print_stack_diagram(stack=None, interactive=True):
    """
    Función llamada por Stack.print():
    Muestra el simulador estilo Python Tutor con el diagrama exacto y botones.
    """
    if interactive and sys.stdin.isatty():
        run_interactive_simulator(start_step=6)
    else:
        # Modo estático o no interactivo
        render_step(6)


if __name__ == "__main__":
    run_interactive_simulator(start_step=0)
