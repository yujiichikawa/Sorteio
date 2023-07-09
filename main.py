from flet import *
from time import sleep
from random import Random, randint


def router(page:Page):
    page.title = "Sorteio"
    page.theme_mode = ThemeMode.LIGHT

    alunos = ["JOAO","HELEN","MARCUS","INAJA","LILLIAN","BARBARA","DEBORA","GABRIEL","MANUELA","VANESSA","ANDERSON MINEIRO","ANDERSON IBURA","GERALDO","THIAGO Y","THIAGO H"]
    participantes_sorteio = []

    lv = ListView(expand=1,
                  spacing=10,
                  item_extent=50,
                  auto_scroll=True)

    controledeSorteio = GridView(expand=True,
        runs_count=6,
        max_extent=175,
        child_aspect_ratio=1.0,
        run_spacing=5,
        auto_scroll=True)

    def verifParticipantes(e):
        if not e.control.value:
            try:
                participantes_sorteio.remove(e.control.label)
            except ValueError:
                print(ValueError)
        elif e.control.value:
            participantes_sorteio.append(e.control.label)

        print(participantes_sorteio)

    def listClassificados():
        controledeSorteio.controls.clear()
        for i in range(len(alunos)):
            controledeSorteio.controls.append(
                Checkbox(
                    label=alunos[i],
                    value=False,
                    on_change=verifParticipantes
                )
            )

        page.update()

    def atualizarLista(e):
        pesq = []
        for i in range(len(alunos)):
            if alunoPesquisa.value.upper() in alunos[i][0:len(alunoPesquisa.value)]:
                pesq.append(alunos[i])

        lv.controls.clear()
        for i in range(len(pesq)):
            lv.controls.append(
                Container(
                    Text(f"{pesq[i]}"),
                    alignment=alignment.center,
                    bgcolor=colors.AMBER_100,
                    border=border.all(2, colors.AMBER_400),
                    padding=5,
                    margin=2
                )
            )

        page.update()

    c1 = Container(
        Text("1", style=TextThemeStyle.HEADLINE_MEDIUM,weight=5),
        alignment=alignment.center,
        width=200,
        height=200,
        bgcolor=colors.TRANSPARENT,
    )
    c2 = Container(
        Text("2", size=50,weight=5),
        alignment=alignment.center,
        width=200,
        height=200,
        bgcolor=colors.TRANSPARENT,
    )
    c3 = Container(
        Text("3", size=50,weight=5),
        alignment=alignment.center,
        width=200,
        height=200,
        bgcolor=colors.TRANSPARENT,
    )
    c = AnimatedSwitcher(
        c1,
        transition=AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=AnimationCurve.BOUNCE_OUT,
        switch_out_curve=AnimationCurve.BOUNCE_IN,
    )

    alunoPesquisa = TextField(
        label="Pesquisar",
        expand=True,
        prefix_text="Aluno(a): ",
        prefix_style= TextStyle(color=colors.RED_400),
        border_radius=20,
        border_width=2,
        border_color=colors.GREY_400,
        on_change=atualizarLista
    )


    qtdLanche = TextField(
        label="Quantidade de lanches",
        expand=False,
        prefix_text="Qtd. ",
        prefix_style=TextStyle(color=colors.ORANGE_400),
        border_radius=20,
        border_color=colors.GREY_400
    )

    def fechar_banner(e):
        page.banner.open = False
        page.update()

    def sleepBanner():
        sleep(3)
        page.banner.open = False
        page.update()

    def excluirAluno(a):
        if not alunoPesquisa.value:
            page.banner = bannervazio
            page.banner.open = True
            page.update()
            sleepBanner()
        elif alunoPesquisa.value.upper() not in alunos:
            page.banner = bannernaoexistente
            page.banner.open = True
            page.update()
            sleepBanner()
        else:
            for i in alunos:
                if i.__eq__(alunoPesquisa.value.upper()):
                    alunos.remove(i)
                    break
            listExcluirAluno()
            page.banner = bannerAlunoExcluido
            page.banner.open = True
            page.update()
            sleepBanner()

    def listAlunos():
        lv.controls.clear()
        for i in range(len(alunos)):
            lv.controls.append(
                Container(
                    Text(f"{alunos[i]}"),
                    alignment=alignment.center,
                    bgcolor=colors.AMBER_100,
                    border=border.all(2, colors.AMBER_400),
                    padding=5,
                    margin=2
                )
            )

        page.update()

    def listExcluirAluno():
        lv.controls.clear()
        for i in range(len(alunos)):
            lv.controls.append(
                Container(
                    Text(alunos[i],color=colors.RED_400),
                    alignment=alignment.center,
                    bgcolor=colors.AMBER_100,
                    border=border.all(2, colors.AMBER_400),
                    padding=5,
                    margin=2,
                )
            )

        page.update()

    bannervazio = Banner(
        bgcolor=colors.AMBER_100,
        leading=Icon(icons.DANGEROUS_SHARP, color=colors.RED_400, size=40),
        content=Text(
            "O Campo abaixo deve ser preenchido"
        ),
        actions=[
            TextButton("OK", on_click=fechar_banner),
        ],
    )

    bannerjaexistente = Banner(
        bgcolor=colors.AMBER_100,
        leading=Icon(icons.DANGEROUS_SHARP, color=colors.RED_400, size=40),
        content=Text(
            "Aluno(a) já existente"
        ),
        actions=[
            TextButton("OK", on_click=fechar_banner),
        ],
    )

    bannerfinalizado = Banner(
        bgcolor=colors.GREEN_400,
        leading=Icon(icons.DANGEROUS_SHARP, color=colors.RED_400, size=40),
        content=Text(
            "Aluno(a) Adicionado"
        ),
        actions=[
            TextButton("OK", on_click=fechar_banner),
        ],
    )

    bannerAlunoExcluido = Banner(
        bgcolor=colors.AMBER_100,
        leading=Icon(icons.DANGEROUS_SHARP, color=colors.RED_400, size=40),
        content=Text(
            "Aluno(a) Excluido "
        ),
        actions=[
            TextButton("OK", on_click=fechar_banner),
        ],
    )

    bannernaoexistente = Banner(
        bgcolor=colors.AMBER_100,
        leading=Icon(icons.DANGEROUS_SHARP, color=colors.RED_400, size=40),
        content=Text(
            "Aluno(a) não encontrado"
        ),
        actions=[
            TextButton("OK", on_click=fechar_banner),
        ],
    )

    bannerInvalido = Banner(
        bgcolor=colors.AMBER_100,
        leading=Icon(icons.DANGEROUS_SHARP, color=colors.RED_400, size=40),
        content=Text(
            "Valor Inválido"
        ),
        actions=[
            TextButton("OK", on_click=fechar_banner),
        ],
    )

    name = TextField(label="Nome", autofocus=True)

    def validacaoNome(name):
        for n in alunos:
            if n.__eq__(name.upper()):
                page.banner = bannerjaexistente
                page.banner.open = True
                page.update()
                sleepBanner()
                break
        else:
            if not name:
                page.banner = bannervazio
                page.banner.open = True
                page.update()
                sleepBanner()
            else:
                alunos.append(name.upper())
                page.banner = bannerfinalizado
                page.banner.open = True
                page.update()
                sleepBanner()

    def cadastrar(e):
        validacaoNome(name.value)
        print(alunos)

    count_txt = Text(value="3", weight=10, color=colors.YELLOW_400,size=200)
    def iniSorteio():
        for i in range(3,-1,-1):
            count_txt.value = str(i)
            page.update()
            sleep(1)
        defsorteados()

    sorteadosResult = []
    def defsorteados():
        for i in range(0,int(qtdLanche.value)):
            num = randint(0,len(participantes_sorteio))
            for i in range(0,len(participantes_sorteio)):
                if num == i:
                    ganhador = participantes_sorteio[i]
                    sorteadosResult.append(ganhador)
        print(sorteadosResult)
    def validacaoQtd(e):
        if not qtdLanche.value:
            page.banner = bannervazio
            page.banner.open = True
            page.update()
            sleepBanner()
        else:
            try:
                qtd = int(qtdLanche.value)
            except ValueError:
                page.banner = bannerInvalido
                page.banner.open = True
                page.update()
                sleepBanner()
                return

            page.go("/resultado")

    def mudancaderotas(route):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    AppBar(
                        leading_width=40,
                        title=Text("Sorteio CDD", color=colors.WHITE),
                        center_title=True,
                        bgcolor=colors.BLUE_400),
                    Row(
                        [
                            ElevatedButton(text="Adicionar Aluno", color=colors.ORANGE_500,
                                           on_click=lambda _: page.go("/addaluno")),
                            ElevatedButton(text="Listar Alunos", color=colors.ORANGE_500,
                                           on_click=lambda _: page.go("/listAluno")),
                            ElevatedButton(text="Remover Aluno", color=colors.ORANGE_500,
                                           on_click= lambda _:page.go("/deleteAluno")),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        [
                            Image(
                                height=400,
                                src="cddv.png",
                                border_radius=50,
                                fit=ImageFit.CONTAIN,
                            )
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                    Row(
                        [
                            ElevatedButton(text="Sorteio", color=colors.WHITE, bgcolor=colors.ORANGE_500, width=200,
                                           height=50,on_click= lambda _:page.go("/sorteio"))
                        ],
                        alignment=MainAxisAlignment.CENTER
                    )
                ],
                scroll=True
            )
        )
        if page.route == "/addaluno":
            page.views.append(
                View(
                    "/addaluno",
                    [
                        AppBar(
                            leading_width=40,
                            title=Text("Cadastro", color=colors.WHITE),
                            center_title=True,
                            bgcolor=colors.BLUE_400,
                        ),

                        Row(
                            [
                                Image(
                                    height=200,
                                    src="cddv.jpeg",
                                    border_radius=50,
                                    fit=ImageFit.CONTAIN,
                                ),
                                Image(
                                    height=100,
                                    src="cddv02.jpeg",
                                    border_radius=50,
                                    fit=ImageFit.CONTAIN,
                                )
                            ],
                            alignment=MainAxisAlignment.CENTER

                        ),
                        Row(
                            controls=[
                                name,
                                ElevatedButton("Adicionar Aluno", on_click=cadastrar)
                            ],
                            alignment=MainAxisAlignment.CENTER,
                        ),

                    ],scroll=True
                )
            )
        elif page.route == "/listAluno":
            listAlunos()
            page.views.append(
                View(
                    "/listAluno",
                    [

                        AppBar(
                            leading_width=40,
                            title=Text("Lista de Alunos", color=colors.WHITE),
                            center_title=True,
                            bgcolor=colors.BLUE_400),
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            controls=[
                                alunoPesquisa
                            ]
                        ),
                        lv
                    ]
                )
            )
        elif page.route == "/deleteAluno":
            listExcluirAluno()
            page.views.append(
                View(
                    "/deleteAluno",
                    [
                        AppBar(
                            leading_width=40,
                            title=Text("Remover Aluno", color=colors.WHITE),
                            center_title=True,
                            bgcolor=colors.BLUE_400),
                        Row(
                            alignment = MainAxisAlignment.CENTER,
                            controls=[
                                alunoPesquisa,
                                IconButton(icon=icons.CLEANING_SERVICES, icon_color=colors.RED_400,on_click=excluirAluno),
                            ]
                        ),
                        lv
                    ]
                )
            )
        elif page.route == "/sorteio":
            participantes_sorteio.clear()
            sorteadosResult.clear()
            listClassificados()
            page.views.append(
                View(
                    "/sorteio",
                    [
                        AppBar(
                            leading_width=40,
                            title=Icon(icons.SELECT_ALL,size=40,color=colors.WHITE),
                            center_title=True,
                            bgcolor=colors.BLUE_400),
                        Row(
                            controls=[
                                Text(value="Alunos a participar",color=colors.ORANGE_400,weight=10,size=50)
                            ],
                            alignment=MainAxisAlignment.CENTER
                        ),
                        Row(
                            controls=[
                                controledeSorteio
                            ]
                        ),
                        Row(
                            controls=[
                                qtdLanche,
                                ElevatedButton(text="Sortear", color=colors.WHITE, bgcolor=colors.ORANGE, on_click= validacaoQtd)
                            ],
                            alignment= MainAxisAlignment.CENTER,
                        )
                    ],scroll=True
                )

            )
        elif page.route == "/resultado":
            page.views.append(
                View(
                    "/resultado",
                    [
                        AppBar(
                            leading_width=40,
                            title=Text(value="Ganhadores",color=colors.WHITE),
                            center_title=True,
                            bgcolor=colors.BLUE_400),

                        Row(
                            controls=[
                                count_txt,
                            ],
                            alignment=MainAxisAlignment.CENTER
                        ),
                    ]
                )
            )
            iniSorteio()

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = mudancaderotas
    page.on_view_pop = view_pop
    page.go(page.route)

app(target=router)
