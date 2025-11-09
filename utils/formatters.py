def format_analysis_result(result):
    formatted = f"""
<b>Отчет анализа</b>

{result['summary']}

<b>Ошибки:</b>
{result['errors'] or 'Нет'}

<b>Рекомендации:</b>
{result['recommendations']}
    """
    return formatted
