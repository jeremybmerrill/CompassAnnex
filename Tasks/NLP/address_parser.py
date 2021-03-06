from __future__ import absolute_import

from vars import CELERY_STUB as celery_app

@celery_app.task
def basicTokenizer(task):
	task_tag = "NLP ADDRESS PARSER"
	print "\n\n************** %s [START] ******************\n" % task_tag
	print "TOKENIZING TEXT DOCUMENT at %s" % task.doc_id
	task.setStatus(412)

	from lib.Worker.Models.uv_document import UnveillanceDocument

	from conf import DEBUG
	from vars import ASSET_TAGS

	doc = UnveillanceDocument(_id=task.doc_id)
	if doc is None:
		print "DOC IS NONE"
		print "\n\n************** %s [ERROR] ******************\n" % task_tag
		return

	txt = None
	if hasattr(task, "txt_file"):
		txt = doc.loadFile(task.txt_file)
	else:
		import os
		try:
			txt_path = doc.getAssetsByTagName(ASSET_TAGS['TXT_JSON'])[0]['file_name']
			txt = doc.loadFile(os.path.join(doc.base_path, txt_path))
		except Exception as e:
			if DEBUG: print e
	
	if txt is None:
		print "TEXT FILE IS NONE"
		print "\n\n************** %s [ERROR] ******************\n" % task_tag
		return
	
	