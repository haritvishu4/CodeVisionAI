from datetime import datetime

def generate_report(data):
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>CodeVision AI Report</title>
        <style>
            body {{
                font-family: Arial;
                background: #f4f4f4;
                padding: 40px;
            }}

            .card {{
                background: white;
                padding: 20px;
                border-radius: 10px;
                width: 500px;
                margin: auto;
                box-shadow: 0 0 10px gray;
            }}

            h1 {{
                color: #2563eb;
            }}

            p {{
                font-size: 18px;
            }}
        </style>
    </head>

    <body>

    <div class="card">

    <h1>🚀 CodeVision AI Report</h1>

    <p><b>Project:</b> {data["project"]}</p>
    <p><b>Total Files:</b> {data["files"]}</p>
    <p><b>Python Files:</b> {data["python"]}</p>
    <p><b>Lines of Code:</b> {data["lines"]}</p>
    <p><b>Functions:</b> {data["functions"]}</p>
    <p><b>Classes:</b> {data["classes"]}</p>

    <hr>

    <p>Generated:
    {datetime.now()}</p>

    </div>

    </body>
    </html>
    """

    with open("reports/report.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("\n✅ HTML Report Generated!")