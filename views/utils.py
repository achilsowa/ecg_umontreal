def get_header(title="Accueil"):
    css = "https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"
    title = f"<title>ECG - UMontreal - {title} </title>"
    meta = "<meta name=""viewport"" content=""width=device-width, initial-scale=1.0, user-scalable=yes"">"
    css = "<link href=""https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css"" rel=""stylesheet"">"
    return f"<head>{title} {meta} {css}</head>"


def get_body(content):
    top = "<header class='d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom'>"
    top += "<a href='/' class='d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none'>"
    top += "<span class='fs-4'>ECG - UMontreal</span></a></header>"

    body = f"<div class='container'><div class='row'> <div class='col-md-12'>{content}</div></div></div>"
    return f"<body>{top} {body}</body>"
