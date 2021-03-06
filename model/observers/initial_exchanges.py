from model.helpers.CsvWriter import CsvWriter
from model.observers.observer import Observer, Observable


class InitialExchanges(Observer):
	POINTER = 0

	def __init__(self, observable):
		super(InitialExchanges, self).__init__(observable)
		self.has_written = False

	def update(self, observable, notification_type: int, **kwargs):

		if notification_type == Observable.START_ROUND:
			self.write_round(kwargs["model"])

	def write_round(self, model):

		model.sort_exchanges()

		if not self.has_written:
			csvwriter = CsvWriter()

			csvwriter.write("data/output/random.{0}.csv".format(InitialExchanges.POINTER), model.Exchanges)

			InitialExchanges.POINTER += 1

			self.has_written = True
