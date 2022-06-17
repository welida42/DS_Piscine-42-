from analytics import Research, Analitics
from config import CONFIG


def ft_report():
    try:
        example = Research(CONFIG["input_file"])
        data = example.file_reader(has_header=CONFIG["has_header"])
        predicts = Analitics(data)
        head_count, tail_count = predicts.counts()
        head_frac, tail_frac = predicts.fractions(head_count, tail_count)

        predicts_data = predicts.predict_random(CONFIG["num_of_steps"])
        our_predicts = Analitics(predicts_data)
        head_predicted, tail_predicted = our_predicts.counts()

        report = CONFIG["report_message"].format((head_count + tail_count), tail_count, head_count,
                round(tail_frac, 2), round(head_frac, 2), CONFIG["num_of_steps"], tail_predicted, head_predicted)

        predicts.save_file(report, CONFIG["output_file"], CONFIG["extension"])

    except Exception as e:
        print(e)


if __name__ == "__main__":
    ft_report()
